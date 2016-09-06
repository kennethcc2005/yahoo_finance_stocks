'''
Download all earning report date data from yahoo finance and rebuild the dataframe with adjusted
earning date.
'''
import requests
import pandas as pd 
import numpy as np 
import datetime as dt
import pandas.io.data as web
from bs4 import BeautifulSoup

def np64toDate(np64):
    return pd.to_datetime(str(np64)).replace(tzinfo=None).to_datetime()

'''
refactor code: look for history er report
'''
datelist = pd.date_range(dt.date(1999,1,27), dt.date.today()).tolist()
datelist = pd.date_range(dt.date(2010,1,27), dt.date.today()).tolist()
df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
for df_date in datelist[::-1]:
    er = str(df_date.date()).replace('-','')
    er_link = 'https://biz.yahoo.com/research/earncal/%s.html' %(er)
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
            df_temp = pd.DataFrame([data] , columns = ['company_name','symbol', 'eps_estimate','time', 'er_date'])
            df = df.append(df_temp)
    except:
        print er_link, 'not a good date'
df = df.reset_index(drop=True)
df.to_pickle('data/20160903_rev_full_history_er_date.pkl')
print 'done! downloaded all data from yahoo finance from 2010 to today'

'''
new er_table starts from year 2012
'''
start = dt.datetime(2012, 1, 1)
end = dt.date.today()
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)

'''DF details from before'''
df_er = pd.read_pickle('data/20160903_rev_full_history_er_date.pkl')
df_new_er = pd.DataFrame(columns = [u'company_name', u'eps_estimate', u'er_date', u'symbol', u'time',
       u'adj_before_er_date', u'adj_after_er_date'])

for i, symbol in enumerate(symbols):
    if i % 100 == 0:
        '''Keep tracking the progress, may take some time to run all stocks'''
        print i, symbol
    try:
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
                '''Drop the earning data if the date too early'''
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
                    '''Drop the current date stock in er, no symbol data for next date'''
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
