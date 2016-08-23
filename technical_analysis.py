import numpy as np 
import pandas as pd 
import json
import time
import pandas.io.data as web
from datetime import date, datetime, timedelta
from collections import defaultdict
start = datetime(2010, 1, 1)
end = date.today()
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
c = web.DataReader("F", 'yahoo', start, end)
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)
prev_er_date = date.today() - timedelta(days = 98)
current_er_date = date.today() - timedelta(days = 10)
symbol = 'AAPL'
class tech_analysis(object):
    def __init__(self,symbol, prev_er_date, current_er_date):
        self.data = web.DataReader(symbol, 'yahoo', prev_er_date, current_er_date)
        self.prev_er_date = prev_er_date
        self.current_er_date = current_er_date

    def on_balance_volume(self):
        '''start_date is the date after the previous earning report and 
        end_date is the date before earning report'''
        data = web.DataReader("AAPL", 'yahoo', self.prev_er_date, self.current_er_date)
        df = data.iloc[1:-1]
        # start_date = self.prev_er_date + timedelta(days = 1)
        # end_date = self.current_er_date - timedelta(days = 1)
        # a = self.data.loc[start_date]
        # df = self.data.reset_index()
        # df = df[df['Date']<= end_date][df['Date']>= start_date]
        # df = df.loc[lambda df1: df1.Date > start_date and df1.Date < end_date, :]
        prev_obv = 0
        p_price = 0
        for i, value in df.iterrows():
            if value['Close'] > p_price:
                current_obv = prev_obv + value['Volume']
            elif value['Close'] < p_price:
                current_obv = prev_obv - value['Volume']
            else:
                current_obv = prev_obv
            p_price = value['Close']
        return current_obv

    def accumulation_distribution(self):
        '''
        There are three steps to calculating the Accumulation Distribution Line (ADL). 
        First, calculate the Money Flow Multiplier. 
        Second, multiply this value by volume to find the Money Flow Volume. 
        Third, create a running total of Money Flow Volume to form the Accumulation Distribution Line (ADL).
        '''
        money_flow_multiplier_day = (self.data.iloc[-1]['Close']-self.data.iloc[-1]['Low'] - (self.data.iloc[-1]['High']-self.data.iloc[-1]['Close'] ))/(self.data.iloc[-1]['High']-self.data.iloc[-1]['Low'])
        money_flow_multiplier_week = (self.data.iloc[-1]['Close']-min(self.data['Low'][-5:]) - (max(self.data['High'][-5:])-self.data.iloc[-1]['Close'] ))/(max(self.data['High'][-5:])-min(self.data['Low'][-5:]))
        money_flow_multiplier_biweek = (self.data.iloc[-1]['Close']-min(self.data['Low'][-10:]) - (max(self.data['High'][-10:])-self.data.iloc[-1]['Close'] ))/(max(self.data['High'][-10:])-min(self.data['Low'][-10:]))
        money_flow_multiplier_quarter = (self.data.iloc[-1]['Close']-min(self.data['Low']) - (max(self.data['High'])-self.data.iloc[-1]['Close'] ))/(max(self.data['High'])-min(self.data['Low']))
        money_flow_vol = None
        ADL = None
        prev_ADL = 0
        return money_flow_multiplier_day, money_flow_multiplier_week, money_flow_multiplier_biweek, money_flow_multiplier_quarter

a = tech_analysis(symbol,prev_er_date, current_er_date)
# print a.on_balance_volume()
print a.accumulation_distribution_line()