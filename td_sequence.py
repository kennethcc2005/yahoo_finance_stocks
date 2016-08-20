import numpy as np 
import pandas as pd 
import json
import pandas.io.data as web
from datetime import date, datetime, timedelta
from collections import defaultdict

class TDSequence(object):
    def __init__(self, data):
        self.data = data

    def sequence(self):
        setup = self.data.iloc[-1]['Close'] - self.data.iloc[-1-4]['Close']
        buy_setup = True
        buy_counter = 1
        sell_counter = -1
        if setup < 0:
            '''buy setup'''
            buy_setup = True
        elif setup > 0:
            '''sell setup'''
            buy_setup = False
        for i in xrange(1,(len(self.data))):
            if buy_setup:
                buy = self.data.iloc[-1-i]['Close'] - self.data.iloc[-5-i]['Close']
                if buy < 0:
                    buy_counter += 1
                    if buy_counter > 9:
                        '''failed to reverse, reset buy counter back to 1'''
                        buy_counter = 1 
                    if buy_counter == 9 and ((self.data.iloc[-2-i]['Close'] - self.data.iloc[-6-i]['Close'])>0):
                        if ((self.data.iloc[-1]['Low'] <= self.data.iloc[-3]['Low']) and (self.data.iloc[-1]['Low'] <= self.data.iloc[-4]['Low'])) or \
                            ((self.data.iloc[-2]['Low'] <= self.data.iloc[-3]['Low']) and (self.data.iloc[-2]['Low'] <= self.data.iloc[-4]['Low'])):
                            buy_counter = 10
                            return buy_counter
                        else:
                            return buy_counter
                else:
                    if (buy_counter == 8) and ((self.data.iloc[-2]['Low'] <= self.data.iloc[-3]['Low']) and (self.data.iloc[-2]['Low'] <= self.data.iloc[-4]['Low'])):
                        buy_counter = 8.5
                        return 8.5
                    else:
                        return buy_counter
            else:
                sell = self.data.iloc[-1-i]['Close'] - self.data.iloc[-5-i]['Close']
                if sell > 0:
                    sell_counter -= 1
                    if sell_counter < -9:
                        '''failed to reverse, reset buy counter back to -1'''
                        sell_counter = -1 
                    if sell_counter == -9 and ((self.data.iloc[-2-i]['Close'] - self.data.iloc[-6-i]['Close'])<0):
                        if ((self.data.iloc[-1]['High'] > self.data.iloc[-3]['High']) and (self.data.iloc[-1]['High'] > self.data.iloc[-4]['High'])) or \
                            ((self.data.iloc[-2]['High'] > self.data.iloc[-3]['High']) and (self.data.iloc[-2]['High'] > self.data.iloc[-4]['High'])):
                            sell_counter = -10
                            return sell_counter
                        else:
                            return sell_counter
                else:
                    if sell_counter == -8 and ((self.data.iloc[-2]['High'] > self.data.iloc[-3]['High']) and (self.data.iloc[-2]['High'] > self.data.iloc[-4]['High'])):
                        sell_counter = -8.5
                        return -8.5
                    else:
                        return sell_counter
        
