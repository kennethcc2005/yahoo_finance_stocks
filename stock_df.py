import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup
import datetime
link = 'https://greenido.wordpress.com/2009/12/22/work-like-a-pro-with-yahoo-finance-hidden-api/'
res = requests.get(link)
soup = BeautifulSoup(res.content, 'html.parser')
# soup.findAll('table')[0].findAll('tr')[0].findAll('span')[0].text
# soup.findAll('table')[0].findAll('tr')[0].findAll('strong')[0].text
f = []
name = []
for j in xrange(29):
    for i in xrange(3):
        try:
            name.append(soup.findAll('table')[0].findAll('tr')[j].findAll('span',style="font-family:times;")[i].text)
            f.append(soup.findAll('table')[0].findAll('tr')[j].findAll('strong')[i].text)
        except:
            print 'out of index'
link_f = ''.join(f)
link_f = link_f.replace(' ','')
#u'aa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1g3g4g5g6ii5j1j3j4j5j6k1k2k3k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p2p5p6qrr1r2r5r6r7ss1s7t1t6t7t8vv1v7ww1w4xy'
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)
stock_list = []
for i in xrange(len(symbols)/1000+1):
    symbol_n = '+'.join(symbols[i*1000:(i+1)*1000]).replace(' ','')
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=aa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1g3g4g5g6ii5j1j3j4j5j6k1k2k3k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p2p5p6qrr1r2r5r6r7ss1s7t1t6t7t8vv1v7ww1w4xy' %(symbol_n)
    df_stock = pd.read_csv(url, header = None)
    df_stock.columns = name
    stock_list.append(df_stock)
df_stocks = pd.concat(stock_list, ignore_index=True)
date = str(datetime.datetime.today().date())
new_name = []
for n in name:
    n = n.encode('ascii', 'ignore').strip()
    new_name.append(n)
df_stock.columns = new_name
csv_name = 'data' + date + '_all_stocks_info.pkl'
df_stocks.to_pickle(csv_name)


