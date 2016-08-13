import numpy as np 
import pandas as pd 
import json
import pandas.io.data as web
from datetime import date, datetime, timedelta
from collections import defaultdict
start = datetime(2010, 1, 1)
end = date.today()
f = web.DataReader("F", 'yahoo', start, end)
df1 = pd.read_csv('companylist.csv')
df2 = pd.read_csv('companylist1.csv')
df3 = pd.read_csv('companylist2.csv')
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)
td_seq = defaultdict()
alert_list = defaultdict()
for symbol in symbols:
    '''
    check the initial td setp up is buy or sell set up then start counting the days.
    '''
    try:
        c = web.DataReader(symbol, 'yahoo', start, end)
        setup = c.iloc[-1]['Close'] - c.iloc[-1-4]['Close']
        # setup = c.ix[str(end-timedelta(days = 1))]['Close'] -  c.ix[str(end-timedelta(days = 4 + 1))]['Close']
        buy_setup = True
        buy_counter = 1
        sell_counter = -1
        if setup < 0:
            '''buy setup'''
            buy_setup = True
        elif setup > 0:
            '''sell setup'''
            buy_setup = False
        for i in xrange(1,(len(c))):
            if buy_setup:
                buy = c.iloc[-1-i]['Close'] - c.iloc[-5-i]['Close']
                # buy = c.ix[str(end-timedelta(days = i))]['Close'] -  c.ix[str(end-timedelta(days = 4 + i))]['Close']
                if buy < 0:
                    buy_counter += 1
                    if buy_counter > 9:
                        buy_counter = 1 
                        print symbol, ' fail to reverse to buy'
                        alert_list[symbol] = buy_counter
                        td_seq[symbol] = buy_counter
                    if buy_counter == 9:
                        if ((c.iloc[-1]['Low'] <= c.iloc[-3]['Low']) and (c.iloc[-1]['Low'] <= c.iloc[-4]['Low'])) or \
                            ((c.iloc[-2]['Low'] <= c.iloc[-3]['Low']) and (c.iloc[-2]['Low'] <= c.iloc[-4]['Low'])):
                            alert_list[symbol] = 'perfect buy'
                        else:
                            alert_list[symbol] = buy_counter
                        td_seq[symbol] = buy_counter
                else:
                    if symbol in alert_list:
                        if (alert_list[symbol] == 'perfect buy') and (buy_counter == 9):
                            print symbol, 'perfect buy'
                    elif buy_counter == 8:
                        if ((c.iloc[-2]['Low'] <= c.iloc[-3]['Low']) and (c.iloc[-2]['Low'] <= c.iloc[-4]['Low'])):
                            alert_list[symbol] = 'prepare perfect buy'
                            print symbol, 'prepare perfect buy'
                    td_seq[symbol] = buy_counter
                    break
            else:
                sell = c.iloc[-1-i]['Close'] - c.iloc[-5-i]['Close']
                # sell = c.ix[str(end-timedelta(days = i))]['Close'] -  c.ix[str(end-timedelta(days = 4 + i))]['Close']
                if sell > 0:
                    sell_counter -= 1
                    if sell_counter < -9:
                        sell_counter = -1 
                        print symbol, ' fail to reverse to sell'
                        alert_list[symbol] = sell_counter
                        td_seq[symbol] = sell_counter
                    if sell_counter == -9:
                        if ((c.iloc[-1]['High'] > c.iloc[-3]['High']) and (c.iloc[-1]['High'] > c.iloc[-4]['High'])) or \
                            ((c.iloc[-2]['High'] > c.iloc[-3]['High']) and (c.iloc[-2]['High'] > c.iloc[-4]['High'])):
                            alert_list[symbol] = 'perfect sell'
                        td_seq[symbol] = sell_counter
                else:
                    if symbol in alert_list:
                        if (alert_list[symbol] == 'perfect sell') and (sell_counter == -9):
                            print symbol, 'perfect sell'
                    elif sell_counter == -8:
                        if ((c.iloc[-2]['High'] > c.iloc[-3]['High']) and (c.iloc[-2]['High'] > c.iloc[-4]['High'])):
                            alert_list[symbol] = 'prepare perfect sell'
                            print symbol, 'prepare perfect sell'
                    td_seq[symbol] = sell_counter
                    break
    except:
        print symbol, ' not in yahoo finance.'
print alert_list
alert_file_name = 'yahoo_finance_stock/' + str(end) +'_alert_list'
td_seq_file_name = 'yahoo_finance_stock/' + str(end) +'_td_seq_list'
with open(alert_file_name, 'w') as f:
    json.dump(alert_list, f)
with open(td_seq_file_name, 'w') as f:
    json.dump(td_seq,f)
