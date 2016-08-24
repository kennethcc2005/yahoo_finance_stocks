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

    def avg_true_range(self):
        '''
        Typically, the Average True Range (ATR) is based on 14 periods and 
        can be calculated on an intraday, daily, weekly or monthly basis. 
        For this example, the ATR will be based on daily data. 
        Because there must be a beginning, the first TR value is simply the High minus the Low, 
        and the first 14-day ATR is the average of the daily TR values for the last 14 days. 
        After that, Wilder sought to smooth the data by incorporating the previous period's ATR value.
        '''
        data_len = self.data.shape[0]
        self.data.iloc[-15]['High'], self.data.iloc[-15]['Low'], self.data.iloc[-15]['Close']
        TRs = []
        pos_DMs = []
        neg_DMs = []
        DXs = []
        for i in xrange(1,data_len):
            high = self.data.iloc[i]['High']
            low = self.data.iloc[i]['Low']
            prev_high = self.data.iloc[i-1]['High']
            prev_close = self.data.iloc[i-1]['Close']
            prev_low = self.data.iloc[i-1]['Low']
            pos_DM1 = max(high-prev_high, 0) if (high-prev_high) > (prev_low - low) else 0
            neg_DM1 = max(prev_low - low, 0) if (prev_low - low) > (high - prev_high) else 0
            TR = max(high-low, abs(high - prev_close), abs(low - prev_close))
            TRs.append(TR)
            pos_DMs.append(pos_DM1)
            neg_DMs.append(neg_DM1)
            if i > 13:
                TR14 = sum(TRs[i-14:])
                pos_DM14 = sum(pos_DMs[i-14:])
                neg_Dm14 = sum(neg_DMs[i-14:])
                pos_DI14 = 100*pos_DM14/TR14
                neg_DI14 = 100*neg_DM14/TR14
                DI14_diff = abs(pos_DI14 - neg_DI14)
                DI14_sum = (pos_DI14 + neg_DI14)
                DX = 100*DI14_diff/DI14_sum
                DXs.append(DX)
                if i > 26:
                    ADX = np.mean(DXs[i-14:])
        return ADX[-1]

    def aroon_indicator(self, days_high = 25):
        '''
        days_high = 25
        '''
        data_len = self.data.shape[0]
        prev_high_ix = np.argmax(self.data['High'][:days_high])
        prev_high = max(self.data['High'][:days_high])
        for i in xrange(days_high, data_len):
            current_high_ix =  np.argmax(self.data['High'][:days_high])
            if (self.data['High'][i] > prev_high) :
                prev_high_ix = i
                prev_high = self.data['High'][i]
            elif i - prev_high_ix >= 25:
                prev_high_ix += np.argmax(self.data['High'][i-24:i+1]) 
                prev_high = max(self.data['High'][i-24:i+1])

            aroon_up = ((days_high - (i-prev_high_ix))/25.)*100
            aroon_down = 
a = tech_analysis(symbol,prev_er_date, current_er_date)
# print a.on_balance_volume()
print a.accumulation_distribution_line()