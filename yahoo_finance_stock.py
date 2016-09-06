'''
Experisemental code for all purposes...
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import datetime as dt


# link = 'https://greenido.wordpress.com/2009/12/22/work-like-a-pro-with-yahoo-finance-hidden-api/'
# res = requests.get(link)
# soup = BeautifulSoup(res.content, 'html.parser')
# soup.findAll('table')

# soup.findAll('table')[0].findAll('tr')[0].findAll('span')[0].text
# soup.findAll('table')[0].findAll('tr')[0].findAll('strong')[0].text
# f = []
# name = []
# for j in xrange(13):
#     for i in xrange(3):
#         name.append(soup.findAll('table')[0].findAll('tr')[j].findAll('span',style="font-family:times;")[i].text)
#         f.append(soup.findAll('table')[0].findAll('tr')[j].findAll('strong')[i].text)
# link_f = ''.join(f)
# link_f = link_f.replace(' ','')
# # u'aa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1g3g4g5g6ii5j1j3j4j5j6k1'

# er_date = str(datelist[-1].date()).replace('-','')
# link = 'https://biz.yahoo.com/research/earncal/%s.html' %(er_date)

# start_er = 'https://biz.yahoo.com/research/earncal/19990119.html'
# start_er = 'https://biz.yahoo.com/research/earncal/20100101.html'
# er_link = 'https://biz.yahoo.com/research/earncal/20161026.html'
# res = requests.get(er_link)
# soup = BeautifulSoup(res.content, 'html.parser')

# try:
#     res = requests.get(er_link)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     try:
#         er_date = soup.find('table', border="0", width="100%", cellpadding="4", cellspacing="0").find('b').text.split('for ')[-1]
#         er_table = soup.find('table',border="0", cellpadding="2", cellspacing="0", width="100%").findAll('tr')[2:-1]
#     except:
#         er_date = soup.find('table', align = 'left').find('font').text.split('\n')[-1]
#         er_table = soup.findAll('tr')[9:-2]
# except:
#     print 'not a good date'

# er_date = soup.find('table', align = 'left').find('font').text.split('\n')[-1]
# er_date = soup.find('table', cellpadding = '2').find('font').text.split('\n')[-1]
# alt_er_date = soup.find('table', border="0", width="100%", cellpadding="4", cellspacing="0").find('b').text.split('for ')[-1]
# for symbol in er_table:
#     for info in symbol.findAll('td')[:-1]:
#         print info.text
# datelist = pd.date_range(dt.date(1999,1,19), dt.date.today()).tolist()

# df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
# data = []
# # er_date = str(dt.date.today()).replace('-','')
# for symbol in er_table:
#     if len(symbol.findAll('td')) == 3:
#         symbol_data = [info.text.replace('\n', ' ') for info in symbol.findAll('td')]
#     else:
#         symbol_data = [info.text for info in symbol.findAll('td')[:-1]]
#     symbol_data.append(er_date)
#     data.append(symbol_data)
# data = np.array(data)
# if data.shape[1] == 4: 
#     df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol', 'time', 'er_date'])
#     df_temp['eps_estimate'] = 'N/A'
#     df.append(df_temp)
# else:
#     df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
#     df.append(df_temp)


'''
refactor code: look for history er report
'''
import requests
from bs4 import BeautifulSoup
datelist = pd.date_range(dt.date(1999,1,27), dt.date.today()).tolist()
datelist = pd.date_range(dt.date(2010,1,27), dt.date.today()).tolist()
df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
for df_date in datelist[::-1]:
    er = str(df_date.date()).replace('-','')
    er_link = 'https://biz.yahoo.com/research/earncal/%s.html' %(er)
#     er_link = 'https://biz.yahoo.com/research/earncal/20161026.html'
#     er_link = 'https://biz.yahoo.com/research/earncal/20100127.html'
    try:
        
        res = requests.get(er_link)
        soup = BeautifulSoup(res.content, 'html.parser')
        try:
            er_date = soup.find('table', border="0", width="100%", cellpadding="4", cellspacing="0").find('b').text.split('for ')[-1]
            er_table = soup.find('table',border="0", cellpadding="2", cellspacing="0", width="100%").findAll('tr')[2:]
        except:
            er_date = soup.find('table', align = 'left').find('font').text.split('\n')[-1]
            er_table = soup.findAll('tr')[9:-2]
        data = []
        # er_date = str(dt.date.today()).replace('-','')
        for symbol in er_table:
            if len(symbol.findAll('td')) == 3:
                symbol_data = [info.text.replace('\n', ' ') for info in symbol.findAll('td')]
                [company_name,symbol,time,] = symbol_data
                eps_estimate = 'N/A'
            elif len(symbol.findAll('td')) == 4:
                symbol_data = [info.text for info in symbol.findAll('td')[:4]]
                [company_name,symbol,time, conference_call] = symbol_data
            else:
                symbol_data = [info.text for info in symbol.findAll('td')[:4]]
                [company_name,symbol,eps_estimate, time] = symbol_data
            data = np.array([company_name,symbol,eps_estimate, time,er_date])
#             print data
            df_temp = pd.DataFrame([data] , columns = ['company_name','symbol', 'eps_estimate','time', 'er_date'])
#             print df_temp
            df = df.append(df_temp)
    except:
        print er_link, 'not a good date'
df = df.reset_index(drop=True)
df.to_pickle('data/20160903_rev_full_history_er_date.pkl')
print 'done!'

'''
new er_table
'''
import pandas as pd 
import numpy as np 
import datetime as dt
import pandas.io.data as web
from decimal import Decimal
from td_sequence import TDSequence
from candle_output import candle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split
from sklearn.metrics import make_scorer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.externals import joblib

'''
Sample data from 2016-07-25, name may changes as date changes
Using AAPL as test
'''
def np64toDate(np64):
    return pd.to_datetime(str(np64)).replace(tzinfo=None).to_datetime()

symbol = 'AAPL'
start = dt.datetime(2012, 1, 1)
end = dt.date.today()
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)

'''DF details from before'''
er_date = '2016-08-16'
c = web.DataReader(symbol, 'yahoo', start, end)
df_er = pd.read_pickle('data/20160903_rev_full_history_er_date.pkl')
df_new_er = pd.DataFrame(columns = [u'company_name', u'eps_estimate', u'er_date', u'symbol', u'time',
       u'adj_before_er_date', u'adj_after_er_date'])
for i, symbol in enumerate(symbols):
    if i % 100 == 0:
        print i, symbol
    try:
        '''sample data detail: AAPL'''
        c = web.DataReader(symbol, 'yahoo', start, end)
        earning_report = df_er[df_er['symbol'] == symbol][:10]
        earning_report['er_date'] = pd.to_datetime(earning_report['er_date'])
        d = c.reset_index()
        adj_before_er_dates = []
        adj_after_er_dates = []
        correct_er_time = []
        drop_index = []
        for ix, time in enumerate(earning_report['time']):
            
            if np64toDate(earning_report['er_date'].values[ix]) < d['Date'][0]:
#                 print symbol, np64toDate(earning_report['er_date'].values[ix]), d['Date'][0]
                drop_index.append(ix)
                continue
            if len(d[d.Date == earning_report['er_date'].values[ix]]) == 0:
                adj_day = 1
                new_date = earning_report['er_date'].iloc[ix] - dt.timedelta(days=adj_day)
                if len(d[d.Date == new_date]) == 0:
                    drop_index.append(ix)
                    continue
                er_index = d[d.Date == new_date].index[0]
                print symbol, 'no good er_date'
            else:
                er_index = d[d.Date == earning_report['er_date'].values[ix]].index[0]
            if 'After' in time or 'pm' in time:
                temp = earning_report['er_date'].iloc[ix]
                if d.iloc[-1]['Date'] == temp:
                    drop_index.append(ix)
                    continue
                after = er_index + 1
                before = er_index
                adj_before_er_dates.append(d.iloc[before]['Date'])
                adj_after_er_dates.append(d.iloc[after]['Date'])
                correct_er_time.append(True)
            elif 'Before' in time or 'am' in time:
                after = er_index
                before = er_index -1
                adj_before_er_dates.append(d.iloc[before]['Date'])
                adj_after_er_dates.append(d.iloc[after]['Date'])
                correct_er_time.append(True)
            else:
                temp = earning_report['er_date'].iloc[ix]
                if d.iloc[-1]['Date'] == temp:
                    drop_index.append(ix)
                    continue
                after = er_index + 1
                before = er_index -1
                adj_before_er_dates.append(d.iloc[before]['Date'])
                adj_after_er_dates.append(d.iloc[after]['Date'])
                correct_er_time.append(False)
        if len(drop_index) > 0 :
            earning_report = earning_report.drop(earning_report.index[drop_index])
        earning_report['adj_before_er_date'] = adj_before_er_dates
        earning_report['adj_after_er_date'] = adj_after_er_dates
        earning_report['correct_er_time'] = correct_er_time
        earning_report.reset_index(drop = True, inplace = True)
        df_new_er = df_new_er.append(earning_report)

    except IOError:
        print symbol
df_new_er.reset_index(drop = True, inplace = True)
df_new_er.to_pickle('data/adjusted_earning_report_hist.pkl')


