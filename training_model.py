import pandas as pd 
import numpy as np 
import datetime as dt
import pandas.io.data as web
from decimal import Decimal

'''
Sample data from 2016-07-25, name may changes as date changes
Using AAPL as test
'''
symbol = 'AAPL'
start = dt.datetime(2012, 1, 1)
end = dt.date.today()
'''DF details from before'''
er_date = '2016-08-16'
c = web.DataReader(symbol, 'yahoo', start, end)
df_stock_detail = pd.read_pickle('data/2016-07-25_all_stocks_info')
df_stock_cash_flow_quarter = pd.read_pickle('data/2016-08-19_cash_flow_quarter.pkl')
df_stock_balance_sheet_quarter = pd.read_pickle('data/2016-08-19_balance_sheet_quarter.pkl')
df_stock_balance_sheet_annual = pd.read_pickle('data/2016-08-19_balance_sheet_annual.pkl')
df_stock_income_statement_quarter = pd.read_pickle('data/2016-08-19_income_statement_quarter.pkl')
df_stock_income_statement_annual = pd.read_pickle('data/2016-08-19_income_statement_quarter.pkl')

df_er = pd.read_pickle('data/rev_full_history_er_date.pkl')

new_col_names = []
for i in df_stock_detail.columns.values:
    new_col_names.append(i.strip())
df_stock_detail.columns = new_col_names

'''sample data detail: AAPL'''
c = web.DataReader(symbol, 'yahoo', start, end)
earning_report = df_er[df_er['symbol'] == symbol][:2]
earning_report['er_date'] = pd.to_datetime(earning_report['er_date'])
earning_report['adj_er_date'] = earning_report['er_date'] if ('After' in earning_report['time'] or 'pm' in earning_report['time'])else earning_report['er_date']-dt.timedelta(days=1)
earning_report.reset_index(drop = True, inplace = True)

for i in xrange(len(earning_report)):
    price = Decimal(c.loc[earning_report['adj_er_date'][i+1]]['Close'])
    symbol_cash_flow_q = df_stock_cash_flow_quarter[df_stock_cash_flow_quarter['symbol'] == symbol]
    symbol_balance_sheet_q = df_stock_balance_sheet_quarter[df_stock_balance_sheet_quarter['symbol'] == symbol]
    symbol_income_statement_q = df_stock_income_statement_quarter[df_stock_income_statement_quarter['symbol'] == symbol]
    symbol_cash_flow_prevQ1 = symbol_cash_flow_q.iloc[i+1]
    symbol_cash_flow_prevQ2 = symbol_cash_flow_q.iloc[i+2]
    symbol_balance_sheet_prevQ1 = symbol_balance_sheet_q.iloc[i+1]
    symbol_balance_sheet_prevQ2 = symbol_balance_sheet_q.iloc[i+2]
    symbol_income_statement_prevQ1 = symbol_income_statement_q.iloc[i+1]

    '''fundamental details'''
    preferred_stock = Decimal(0 if symbol_balance_sheet_prevQ1['Redeemable Preferred Stock, Total'] == None else symbol_balance_sheet_prevQ1['Redeemable Preferred Stock, Total']) \
                        + Decimal(0 if symbol_balance_sheet_prevQ1['Preferred Stock - Non Redeemable, Net'] == None else symbol_balance_sheet_prevQ1['Preferred Stock - Non Redeemable, Net']) 
    book_value = (symbol_balance_sheet_prevQ1['Total Equity'] - preferred_stock ) / symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']
    free_cash_flow = (symbol_cash_flow_prevQ1['Cash from Operating Activities'] + symbol_cash_flow_prevQ1['Capital Expenditures'])
    total_revenue = symbol_income_statement_prevQ1['Total Revenue']
    net_income = symbol_income_statement_prevQ1['Net Income']
    debt = symbol_balance_sheet_prevQ1['Total Long Term Debt']
    equity = symbol_balance_sheet_prevQ1['Total Equity']

    '''value investing'''
    price_to_book_value_q = price/book_value
    price_to_free_cash_flow_q = price/free_cash_flow
    price_to_earnings_q = price / symbol_income_statement_prevQ1['Diluted Normalized EPS']
    price_to_sales_q = total_revenue / symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']
    dividends = symbol_income_statement_prevQ1['Dividends per Share - Common Stock Primary Issue']
    long_term_debt_quarter = symbol_balance_sheet_prevQ1['Long Term Debt']
    # long_term_debt_annual = symbol_balance_sheet_annual['Long Term Debt']
    if max(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'],symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) / min(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'], symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) >= 2:
        capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']
    else:
        capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']
    market_cap = symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] * price
    return_on_total_capital =  (net_income - dividends * symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']) / (debt + equity)
    return_on_shareholders_equity = net_income/equity 
    extra_shares_outstanding = symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']

    '''td_sequential'''

    '''candle_stick'''
# Below are for futrue test data...not useful for training with lack of data
# symbol_detail = df_stock_detail[df_stock_detail['Symbol'] == symbol]
# symbol_quarter_idx = symbol+'_prev_1Q'
# temp = symbol+'_' + str(dt.date.today().year)
# temp2 = symbol+'_' + str(dt.date.today().year-1)
# if temp in df_stock_balance_sheet_annual.index:
#   symbol_annual_idx = temp
# elif temp2 in df_stock_balance_sheet_annual.index:
#     symbol_annual_idx = temp2
# else:
#     symbol_annual_idx = symbol+'_' + str(dt.date.today().year-2)

# symbol_cash_flow_prevQ1 = df_stock_cash_flow_quarter.ix[symbol_quarter_idx]
# symbol_balance_sheet_annual = df_stock_balance_sheet_annual.ix[symbol_annual_idx]
# symbol_balance_sheet_prevQ1 = df_stock_balance_sheet_quarter.ix[symbol_quarter_idx]
# symbol_balance_sheet_prevQ2 = df_stock_balance_sheet_quarter.ix[symbol+'_prev_2Q']
# symbol_cash_flow_prevQ1 = df_stock_cash_flow_quarter.ix[symbol_quarter_idx]
# symbol_cash_flow_prevQ2 = df_stock_cash_flow_quarter.ix[symbol+'_prev_2Q']

# '''value investing'''
# price_to_book_value = symbol_detail['Price/Book']
# price_to_free_cash_flow_prevQ1 = c['Adj Close'][er_date]/(symbol_cash_flow_prevQ1['Cash from Operating Activities'] + symbol_cash_flow_prevQ1['Capital Expenditures'])
# price_to_earnings = symbol_detail['P/E Ratio']
# price_to_sales = symbol_detail['Price/Sales']
# dividends = symbol_detail['Dividend/Share']
# long_term_debt_quarter = symbol_balance_sheet_prevQ1['Long Term Debt']
# long_term_debt_annual = symbol_balance_sheet_annual['Long Term Debt']

# if max(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'],symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) / min(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'], symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) >= 2:
#     capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']
# else:
#     capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']

# market_cap = symbol_detail['Market Capitalization']
# shares_outstanding = symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']

