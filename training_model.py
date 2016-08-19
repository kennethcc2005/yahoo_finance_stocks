import pandas as pd 
import numpy as np 
import datetime as dt
import pandas.io.data as web
'''
Sample data from 2016-07-25, name may changes as date changes
Using AAPL as test
'''
symbol = 'AAPL'
start = dt.datetime(2010, 1, 1)
end = dt.date.today()
'''DF details from before'''
er_date = '2016-08-16'
c = web.DataReader(symbol, 'yahoo', start, end)
df_stock_detail = pd.read_pickle('data/2016-07-25_all_stocks_info')
df_stock_cash_flow_quarter = pd.read_pickle('data/2016-08-18_cash_flow_quarter.pkl')
df_stock_balance_sheet_quarter = pd.read_pickle('data/2016-08-18_balance_sheet_quarter.pkl')
df_stock_balance_sheet_annual = pd.read_pickle('data/2016-08-18_balance_sheet_annual.pkl')

'''Clean df_stock_detail column names to strip spaces: 
Index([u'Ask', u'Average Daily Volume', u'Ask Size', u'Bid',
       u'Ask (Real-time)', u'Bid (Real-time)', u'Book Value', u'Bid Size',
       u'Change & Percent Change', u'Change', u'Commission',
       u'Change (Real-time)', u'After Hours Change (Real-time)',
       u'Dividend/Share', u'Last Trade Date', u'Trade Date', u'Earnings/Share',
       u'Error Indication (returned for symbol changed / invalid)',
       u'EPS Estimate Current Year', u'EPS Estimate Next Year',
       u'EPS Estimate Next Quarter', u'Float Shares', u'Day’s Low',
       u'Day’s High', u'52-week Low', u'52-week High',
       u'Holdings Gain Percent', u'Annualized Gain', u'Holdings Gain',
       u'Holdings Gain Percent (Real-time)', u'Holdings Gain (Real-time)',
       u'More Info', u'Order Book (Real-time)', u'Market Capitalization',
       u'Market Cap (Real-time)', u'EBITDA', u'Change From 52-week Low',
       u'Percent Change From 52-week Low', u'Last Trade (Real-time) With Time',
       u'Change Percent (Real-time)', u'Last Trade Size',
       u'Change From 52-week High', u'Percebt Change From 52-week High',
       u'Last Trade (With Time)', u'Last Trade (Price Only)', u'High Limit',
       u'Low Limit', u'Day’s Range', u'Day’s Range (Real-time)',
       u'50-day Moving Average', u'200-day Moving Average',
       u'Change From 200-day Moving Average',
       u'Percent Change From 200-day Moving Average',
       u'Change From 50-day Moving Average',
       u'Percent Change From 50-day Moving Average', u'Name', u'Notes',
       u'Open', u'Previous Close', u'Price Paid', u'Change in Percent',
       u'Price/Sales', u'Price/Book', u'Ex-Dividend Date', u'P/E Ratio',
       u'Dividend Pay Date', u'P/E Ratio (Real-time)', u'PEG Ratio',
       u'Price/EPS Estimate Current Year', u'Price/EPS Estimate Next Year',
       u'Symbol', u'Shares Owned', u'Short Ratio', u'Last Trade Time',
       u'Trade Links', u'Ticker Trend', u'1 yr Target Price', u'Volume',
       u'Holdings Value', u'Holdings Value (Real-time)', u'52-week Range',
       u'Day’s Value Change', u'Day’s Value Change (Real-time)',
       u'Stock Exchange', u'Dividend Yield'],
      dtype='object')'''
new_col_names = []
for i in df_stock_detail.columns.values:
    new_col_names.append(i.strip())
df_stock_detail.columns = new_col_names

'''
Cash Flow columns:

'''

'''sample data detail: AAPL'''
symbol_detail = df_stock_detail[df_stock_detail['Symbol'] == symbol]
symbol_quarter_idx = symbol+'_prev_1Q'
temp = symbol+'_' + str(dt.date.today().year)
temp2 = symbol+'_' + str(dt.date.today().year-1)

if temp in df_stock_balance_sheet_annual.index:
    symbol_annual_idx = temp
elif temp2 in df_stock_balance_sheet_annual.index:
    symbol_annual_idx = temp2
else:
    symbol_annual_idx = symbol+'_' + str(dt.date.today().year-2)

symbol_cash_flow_prevQ1 = df_stock_cash_flow_quarter.ix[symbol_quarter_idx]
symbol_balance_sheet_annual = df_stock_balance_sheet_annual.ix[symbol_annual_idx]
symbol_balance_sheet_prevQ1 = df_stock_balance_sheet_quarter.ix[symbol_quarter_idx]
symbol_balance_sheet_prevQ2 = df_stock_balance_sheet_quarter.ix[symbol+'_prev_2Q']
symbol_cash_flow_prevQ1 = df_stock_cash_flow_quarter.ix[symbol_quarter_idx]
symbol_cash_flow_prevQ2 = df_stock_cash_flow_quarter.ix[symbol+'_prev_2Q']

'''value investing'''
price_to_book_value = symbol_detail['Price/Book']
price_to_free_cash_flow_prevQ1 = c['Adj Close'][er_date]/(symbol_cash_flow_prevQ1['Cash from Operating Activities'] + symbol_cash_flow_prevQ1['Capital Expenditures'])
price_to_earnings = symbol_detail['P/E Ratio']
price_to_sales = symbol_detail['Price/Sales']
dividends = symbol_detail['Dividend/Share']
long_term_debt_quarter = symbol_balance_sheet_prevQ1['Long Term Debt']
long_term_debt_annual = symbol_balance_sheet_annual['Long Term Debt']

if max(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'],symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) / min(symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'], symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']) >= 2:
    capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding']
else:
    capital_spending_diff = symbol_cash_flow_prevQ1['Capital Expenditures']/symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_cash_flow_prevQ2['Capital Expenditures']/symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']

market_cap = symbol_detail['Market Capitalization']
shares_outstanding = symbol_balance_sheet_prevQ1['Total Common Shares Outstanding'] - symbol_balance_sheet_prevQ2['Total Common Shares Outstanding']

