
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import datetime as dt

link = 'https://greenido.wordpress.com/2009/12/22/work-like-a-pro-with-yahoo-finance-hidden-api/'
res = requests.get(link)
soup = BeautifulSoup(res.content, 'html.parser')
soup.findAll('table')

soup.findAll('table')[0].findAll('tr')[0].findAll('span')[0].text
soup.findAll('table')[0].findAll('tr')[0].findAll('strong')[0].text
f = []
name = []
for j in xrange(13):
    for i in xrange(3):
        name.append(soup.findAll('table')[0].findAll('tr')[j].findAll('span',style="font-family:times;")[i].text)
        f.append(soup.findAll('table')[0].findAll('tr')[j].findAll('strong')[i].text)
link_f = ''.join(f)
link_f = link_f.replace(' ','')
# u'aa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1g3g4g5g6ii5j1j3j4j5j6k1'
er_date = str(datelist[-1].date()).replace('-','')
link = 'https://biz.yahoo.com/research/earncal/%s.html' %(er_date)

start_er = 'https://biz.yahoo.com/research/earncal/19990119.html'
er_link = 'https://biz.yahoo.com/research/earncal/20161026.html'
res = requests.get(er_link)
soup = BeautifulSoup(res.content, 'html.parser')

try:
    res = requests.get(er_link)
    soup = BeautifulSoup(res.content, 'html.parser')
    try:
        er_date = soup.find('table', border="0", width="100%", cellpadding="4", cellspacing="0").find('b').text.split('for ')[-1]
        er_table = soup.find('table',border="0", cellpadding="2", cellspacing="0", width="100%").findAll('tr')[2:-1]
    except:
        er_date = soup.find('table', align = 'left').find('font').text.split('\n')[-1]
        er_table = soup.findAll('tr')[9:-2]
except:
    print 'not a good date'

# er_date = soup.find('table', align = 'left').find('font').text.split('\n')[-1]
# er_date = soup.find('table', cellpadding = '2').find('font').text.split('\n')[-1]
# alt_er_date = soup.find('table', border="0", width="100%", cellpadding="4", cellspacing="0").find('b').text.split('for ')[-1]
for symbol in er_table:
    for info in symbol.findAll('td')[:-1]:
        print info.text
datelist = pd.date_range(dt.date(1999,1,19), dt.date.today()).tolist()

df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
data = []
# er_date = str(dt.date.today()).replace('-','')
for symbol in er_table:
    if len(symbol.findAll('td')) == 3:
        symbol_data = [info.text.replace('\n', ' ') for info in symbol.findAll('td')]
    else:
        symbol_data = [info.text for info in symbol.findAll('td')[:-1]]
    symbol_data.append(er_date)
    data.append(symbol_data)
data = np.array(data)
if data.shape[1] == 4: 
    df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol', 'time', 'er_date'])
    df_temp['eps_estimate'] = 'N/A'
    df.append(df_temp)
else:
    df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
    df.append(df_temp)


'''
refactor code:
'''
datelist = pd.date_range(dt.date(1999,1,27), dt.date.today()).tolist()
df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
for df_date in datelist[:100]:
    er = str(df_date.date()).replace('-','')
    er_link = 'https://biz.yahoo.com/research/earncal/%s.html' %(er)
#     er_link = 'https://biz.yahoo.com/research/earncal/20161026.html'
#     er_link = 'https://biz.yahoo.com/research/earncal/19990127.html'
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
            else:
                symbol_data = [info.text for info in symbol.findAll('td')[:-1]]
            symbol_data.append(er_date)
            data.append(symbol_data)
        data = np.array(data)
        if data.shape[1] == 4: 
            df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol', 'time', 'er_date'])
            df_temp['eps_estimate'] = 'N/A'
            df = df.append(df_temp)
        else:
            df_temp = pd.DataFrame(data = data, columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
            df = df.append(df_temp)
    except:
        print df_date, 'not a good date'
df = df.reset_index(drop=True)