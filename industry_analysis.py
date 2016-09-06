'''
Industry analysis with current symbol stand in sector and industry ranking and movements.
'''
import pandas as pd 
import numpy as np 
import datetime as dt
import pandas.io.data as web

'''
Sample data from 2016-07-25, name may changes as date changes
Using AAPL as test
'''
symbol = 'AAPL'
start = dt.datetime(2012, 1, 1)
end = dt.date.today()
df_er = pd.read_pickle('data/adjusted_earning_report_hist.pkl')
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
dfs = df1.append(df2).append(df3)
dfs.drop('Unnamed: 8', axis = 1, inplace =True)
dfs.set_index('Symbol',inplace = True)

for symbol in dfs.index:
    symbol_market_cap = dfs.loc[symbol]['MarketCap'].replace('$','').replace('M','')
    if 'B' in symbol_market_cap:
        symbol_market_cap = float(a.replace('B', ''))*1000
    elif symbol_market_cap == 'n/a':
        symbol_market_cap = 0
    symbol_market_cap = float(symbol_market_cap)
    industry = dfs.loc[symbol]['industry']
    industry_symbols = dfs[dfs['industry'] == dfs.loc[symbol]['industry']].index.values
    sector_symbols = dfs[dfs['Sector'] == dfs.loc[symbol]['Sector']].index.values
    total_ind_mkt_cap = 0
    total_sector_mkt_cap = 0
    rank_industry = 1
    rank_sector = 1
    for symbol_i in industry_symbols:
        # c = web.DataReader(symbol, 'yahoo', start, end)
        a = dfs.loc[symbol_i]['MarketCap'].replace('$','').replace('M','')
        if 'B' in a:
            a = float(a.replace('B', ''))*1000
        elif a == 'n/a':
            a = 0
        if  float(a) > symbol_market_cap:
            rank_industry += 1
        total_ind_mkt_cap += float(a)

    for symbol_s in sector_symbols:
        # c = web.DataReader(symbol, 'yahoo', start, end)
        a = dfs.loc[symbol_s]['MarketCap'].replace('$','').replace('M','')
        if 'B' in a:
            a = float(a.replace('B', ''))*1000
        elif a == 'n/a':
            a = 0
        if  float(a) > symbol_market_cap:
            rank_sector += 1
        total_sector_mkt_cap += float(a)

    avg_industry_mkt_cap = total_ind_mkt_cap/len(industry_symbols)
    avg_sector_mkt_cap = total_sector_mkt_cap/len(sector_symbols)
    avg_move_industry_er = None
    avg_move_sector_er = None





