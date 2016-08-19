import numpy as np 
import pandas as pd 
import json
import time
import pandas.io.data as web
from datetime import date, datetime, timedelta
from collections import defaultdict
from google_finance import GoogleFinance as GF

# price_to_book_value = df[' Price/Book ']
price_to_cash_flow = None
price_to_earnings = None
price_to_sales = None
dividends = None
begin_time = datetime.today()
'''
Google is smart to detect which market for the symbols...Default to nasdaq
'''
market = 'NASDAQ'
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)
google_finance = GF(market, 'AAPL')
balance_sheet_a = google_finance.balance_sheet('annual')
balance_sheet_q = google_finance.balance_sheet('interim')
income_statement_a = google_finance.income_statement('annual')
income_statement_q = google_finance.income_statement('interim')
cash_flow_a = google_finance.cash_flow('annual')
cash_flow_q = google_finance.cash_flow('interim')
col_names_bs = list(balance_sheet_a[0][1:])
col_names_bs.extend(['symbol','date'])
col_names_is = list(income_statement_a[0][1:])
col_names_is.extend(['symbol','date'])
col_names_cf = list(cash_flow_a[0][1:])
col_names_cf.extend(['symbol','date'])
df_bs_a = pd.DataFrame(columns = col_names_bs)
df_bs_q = pd.DataFrame(columns = col_names_bs)
df_is_a = pd.DataFrame(columns = col_names_is)
df_is_q = pd.DataFrame(columns = col_names_is)
df_cf_a = pd.DataFrame(columns = col_names_cf)
df_cf_q = pd.DataFrame(columns = col_names_cf)
count_ = 0
failed_list = []
for symbol in symbols:
    '''
    check the google finance to download financial statements into df.
    '''
    try:
        google_finance = GF(market, symbol)
        balance_sheet_a = google_finance.balance_sheet('annual')
        balance_sheet_q = google_finance.balance_sheet('interim')
        income_statement_a = google_finance.income_statement('annual')
        income_statement_q = google_finance.income_statement('interim')
        cash_flow_a = google_finance.cash_flow('annual')
        cash_flow_q = google_finance.cash_flow('interim')
        quarter_names = ['prev_1Q','prev_2Q','prev_3Q','prev_4Q','prev_5Q','prev_6Q']
        for item in balance_sheet_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_bs_a.ix[idx] = row

        for item in income_statement_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_is_a.ix[idx] = row

        for item in cash_flow_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_cf_a.ix[idx] = row

        for i, item in enumerate(balance_sheet_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_bs_q.ix[idx] = row

        for i, item in enumerate(income_statement_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_is_q.ix[idx] = row

        for i, item in enumerate(cash_flow_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_cf_q.ix[idx] = row
        count_ += 1
        if count_ % 10 == 0:
            time.sleep(6)
            print count_
    except:
        failed_list.append(symbol)
        print symbol, ' not in google finance.'

for symbol in failed_list:
    try:
        google_finance = GF(market, symbol)
        balance_sheet_a = google_finance.balance_sheet('annual')
        balance_sheet_q = google_finance.balance_sheet('interim')
        income_statement_a = google_finance.income_statement('annual')
        income_statement_q = google_finance.income_statement('interim')
        cash_flow_a = google_finance.cash_flow('annual')
        cash_flow_q = google_finance.cash_flow('interim')
        quarter_names = ['prev_1Q','prev_2Q','prev_3Q','prev_4Q','prev_5Q','prev_6Q']
        for item in balance_sheet_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_bs_a.ix[idx] = row

        for item in income_statement_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_is_a.ix[idx] = row

        for item in cash_flow_a[1:]:
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + str(item[0].year)
            df_cf_a.ix[idx] = row

        for i, item in enumerate(balance_sheet_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_bs_q.ix[idx] = row

        for i, item in enumerate(income_statement_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_is_q.ix[idx] = row

        for i, item in enumerate(cash_flow_q[1:7]):
            row = list(item[1:])
            row.extend([symbol, item[0]])
            idx = symbol + '_' + quarter_names[i]
            df_cf_q.ix[idx] = row
        count_ += 1
        if count_ % 10 == 0:
            time.sleep(6)
            print count_
    except:
        print symbol, 'again not in google finance.'
end_time = datetime.today()
print str(end_time - begin_time)
'''
PCTY  not in google finance.
PYDS  not in google finance.
PYPL  not in google finance.
PBBI  not in google finance.
PCCC  not in google finance.
PCMI  not in google finance.
PCTI  not in google finance.
PDCE  not in google finance.
PDFS  not in google finance.
PDLI  not in google finance.
PDVW  not in google finance.
SKIS  not in google finance.
PGC  not in google finance.
PEGA  not in google finance.
PCO  not in google finance.
'''
df_bs_a.to_pickle('data/' + str(date.today())+'_'+'balance_sheet_annual.pkl')
df_bs_q.to_pickle('data/' + str(date.today())+'_'+'balance_sheet_quarter.pkl')
df_is_a.to_pickle('data/' + str(date.today())+'_'+'income_statement_annual.pkl')
df_is_q.to_pickle('data/' + str(date.today())+'_'+'income_statement_quarter.pkl')
df_cf_a.to_pickle('data/' + str(date.today())+'_'+'cash_flow_annual.pkl')
df_cf_q.to_pickle('data/' + str(date.today())+'_'+'cash_flow_quarter.pkl')
