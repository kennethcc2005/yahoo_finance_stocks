import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import datetime as dt

current_df = pd.read_pickle('current_er_calendar.pkl')
datelist = pd.date_range(dt.date.today(), dt.date.today() + dt.timedelta(days=60)).tolist()
df = pd.DataFrame(columns = ['company_name','symbol','eps_estimate', 'time', 'er_date'])
for df_date in datelist:
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
            else:
                symbol_data = [info.text for info in symbol.findAll('td')[:4]]
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
        print er_link, 'not a good date'
df.set_index('symbol', inplace= True)
results = current_df.combine_first(df)
results.update(df)
results.to_pickle('current_er_calendar.pkl')