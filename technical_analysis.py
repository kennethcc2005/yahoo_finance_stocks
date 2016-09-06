'''
Technical analysis with popular indicators
'''
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
        self.data = web.DataReader(symbol, 'yahoo', prev_er_date + timedelta(days = 1), current_er_date)
        self.prev_er_date = prev_er_date + timedelta(days = 1)
        self.current_er_date = current_er_date

    def on_balance_volume(self):
        '''start_date is the date after the previous earning report and 
        end_date is the date before earning report'''
        data = web.DataReader("AAPL", 'yahoo', self.prev_er_date, self.current_er_date)
        df = data
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
        The Aroon osciallatro is a technical indicator used to measure if a security is in a trend, 
        and the magnitude of that trend. The indicator can also be used to identify when a new trend is set to begin. 
        The indicator is comprised of two lines: an Aroon-up line and an Aroon-down line. 
        A security is considered to be in an uptrend when the Aroon-up line is above 70, along with being above the Aroon-down line. 
        The security is in a downtrend when the Aroon-down line is above 70 and also above the Aroon-up line.
        '''
        data_len = self.data.shape[0]
        prev_high_ix = np.argmax(self.data['High'][:days_high+1])
        prev_high = max(self.data['High'][:days_high])
        prev_low_ix = np.argmin(self.data['Low'][:days_high+1])
        prev_low = min(self.data['Low'][:days_high])
        aroon_ups = []
        aroon_downs = []
        for i in xrange(days_high, data_len):
            if (self.data['High'][i] > prev_high) :
                prev_high_ix = i
                prev_high = self.data['High'][i]
            elif i - prev_high_ix > days_high:
                prev_high_ix += np.argmax(self.data['High'][i-days_high:i+1]) 
                prev_high = max(self.data['High'][i-days_high:i+1])
            if (self.data['Low'][i] < prev_low):
                prev_low_ix = i
                prev_low = self.data['Low'][i]
            elif i - prev_low_ix > days_high:
                prev_low_ix += np.argmin(self.data['Low'][i-days_high:i+1]) 
                prev_low = min(self.data['Low'][i-days_high:i+1])
            aroon_up = ((days_high - (i-prev_high_ix))/float(days_high))*100
            aroon_down = ((days_high - (i-prev_low_ix))/float(days_high))*100
            aroon_ups.append(aroon_up)
            aroon_downs.append(aroon_down)
        return aroon_ups, aroon_downs

    def MACD(self, EMA1_ = 12, EMA2_ = 26):
        '''
        Moving average convergence divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of prices. 
        The MACD is calculated by subtracting the 26-day exponential moving average (EMA) from the 12-day EMA. 
        A nine-day EMA of the MACD, called the "signal line", is then plotted on top of the MACD, functioning as a trigger for buy and sell signals.
        '''
        EMA1 = self.EMA_(period = EMA1_)
        EMA2 = self.EMA_(period = EMA2_)
        MACDs = []
        for i in xrange(len(EMA2)):
            MACD = EMA1[EMA2_ - EMA1_ + i] - EMA2[i]
            MACDs.append(MACD)
        signals = self.EMA_(period = 9, data = MACDs)
        return MACDs, signals

    def EMA_(self,period = 10, data = self.data['Close']):
        SMA = sum(data[:period])/float(period)
        mult = (2 / float(period + 1) )
        EMA = SMA
        EMAs = [EMA]
        for i in xrange(period+1, len(data['Close'])+1):
            SMA = sum(data['Close'][i-period:i])/float(period)
            EMA = (data['Close'][i-1] - EMA) * mult + EMA
            EMAs.append(EMA)
        return EMAs

    def SMA_(self,period = 10, data =self.data['Close']):
        SMAs = []
        for i in xrange(period, len(data)):
            SMA = sum(data[i-period:i])/float(period)
            SMAs.append(SMA)
        return SMAs

    def RSI(self,period = 14):
        '''
        Relative Strength Index (RSI) is an extremely popular momentum indicator that has been featured in a number of articles, 
        interviews and books over the years. In particular, Constance Brown's book, 
        Technical Analysis for the Trading Professional, features the concept of bull market and bear market ranges for RSI. 
        Andrew Cardwell, Brown's RSI mentor, introduced positive and negative reversals for RSI. 
        In addition, Cardwell turned the notion of divergence, literally and figuratively, on its head.
        '''
        gains = []
        losses = []
        avg_gains = []
        avg_losses = []
        RSs = []
        RSIs = []
        for i in xrange(1,self.data.shape[0]):
            change = self.data['Close'][i] - self.data['Close'][i-1]
            if change < 0:
                losses.append(abs(change))
                gains.append(0)
            else:
                gains.append(change)
                losses.append(0)
            if i >= period:
                avg_gain = np.mean(gains[i-period+1:])
                avg_loss = np.mean(losses[i-period+1:])
                RS = avg_gain / avg_loss if avg_loss != 0 else 99999
                RSI = 0 if avg_loss == 0 else 100 - (100/(1+RS))
                RSs.append(RS)
                RSIs.append(RSI)
                avg_gains.append(avg_gain)
                avg_losses.append(avg_loss)
        return RSs,RSIs

    def stochastic_oscillator(self,period = 14):
        '''

        K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
        D = 3-day SMA of K

        Lowest Low = lowest low for the look-back period
        Highest High = highest high for the look-back period
        K is multiplied by 100 to move the decimal point two places
        '''
        stochastic_oscillators = []
        for i in xrange(period,self.data.shape[0]+1):
            high = max(slef.data['High'][i - 14, i])
            low = min(slef.data['Low'][i - 14, i])
            current_close = slef.data['Close'][i-1]
            sc = (current_close-low)/(high-low)*100
            stochastic_oscillators.append(sc)

        D = self.SMA_(period = 3, data = stochastic_oscillators)
        return stochastic_oscillators, D

    def chaikin_money_flow(self, period = 20):
        '''
          1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 
          2. Money Flow Volume = Money Flow Multiplier x Volume for the Period
          3. 20-period CMF = 20-period Sum of Money Flow Volume / 20 period Sum of Volume 
        '''
        mf_vols =[]
        CMFs = []
        vols = []
        for i in xrange(self.data.shape[0]):
            mf_mult = ((self.data['Close'][i] - self.data['Low'][i]) - (self.data['High'][i] - self.data['Close'][i]))/(self.data['High'][i] - self.data['Low'][i])
            mf_vol = mf_mult * self.data['Volume'][i]
            vols.append(self.data['Volume'][i])
            mf_vols.append(mf_vol)
            if i >= 19:
                cmf = sum(mf_vols[i-period+1:i+1])/sum(vols[i-period+1:i+1])
                CMFs.append(cmf)
        return CMFs

    def price_relative(self,symbol = 'SPY'):
        '''
        Price Relative = Base Security / Comparative Security
        Ratio Symbol Close = Close of First Symbol / Close of Second Symbol
        Ratio Symbol Open  = Open of First Symbol / Close of Second Symbol
        Ratio Symbol High  = High of First Symbol / Close of Second Symbol
        Ratio Symbol Low   = Low of First Symbol / Close of Second Symbol
        '''
        second_data = web.DataReader(symbol, 'yahoo', self.prev_er_date, self.current_er_date)
        changes = []
        diffs = []
        for i in xrange(1,self.data['Close']):
            prev_price_rel = self.data['Close'][i-1] / second_data['Close'][i-1]
            price_rel = self.data['Close'][i] / second_data['Close'][i]
            change_price_rel = (price_rel - prev_price_rel)/prev_price_rel
            change_data = (self.data['Close'][i] - self.data['Close'][i-1]) / self.data['Close'][i-1]
            change_second_data = (second_data['Close'][i] - second_data['Close'][i-1]) / second_data['Close'][i-1]
            diff = change_data - change_second_data
            changes.append(change_price_rel)
            diffs.append(diff)
        return changes, diffs

a = tech_analysis(symbol,prev_er_date, current_er_date)
# print a.on_balance_volume()
print a.accumulation_distribution_line()