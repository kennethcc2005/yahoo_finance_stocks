'''
Candlestick pattern functions in class type. 
Only need to run output function to build the dataframe for all patterns for one symbol.
'''
import numpy as np
import pandas as pd
import json
import pandas.io.data as web
from datetime import date, datetime, timedelta
from collections import defaultdict
start = datetime(2010, 1, 1)
end = date.today()
df1 = pd.read_csv('data/companylist.csv')
df2 = pd.read_csv('data/companylist1.csv')
df3 = pd.read_csv('data/companylist2.csv')
data = web.DataReader("F", 'yahoo', start, end)
symbols = np.append(df1.Symbol.values, df2.Symbol.values)
symbols = np.append(symbols, df3.Symbol.values)

class candle(object):
    def __init__(self,data):
        self.data=data
    def output(self):
          out_df=pd.DataFrame(index=[0])
          out_df['a_new_price']=self.eight_new_price()
          out_df['eight_new_price']=self.eight_new_price()
          out_df['ten_new_price']=self.ten_new_price()
          out_df['twelve_new_price']=self.twelve_new_price()
          out_df['thirteen_new_price']=self.thirteen_new_price()
          out_df['bearish_abandoned_baby']=self.bearish_abandoned_baby()
          out_df['bullish_abandoned_baby']=self.bullish_abandoned_baby()
          out_df['above_stomach']=self.above_stomach()
          out_df['advance_block']=self.advance_block()
          out_df['below_stomach']=self.below_stomach()
          out_df['bearish_belt_hold']=self.bearish_belt_hold()
          out_df['bearish_breakaway']=self.bearish_breakaway()
          out_df['bearish_doji_star']=self.bearish_doji_star()
          out_df['bearish_engulfing']=self.bearish_engulfing()
          out_df['bearish_harami']=self.bearish_harami()
          out_df['bearish_harami_cross']=self.bearish_harami_cross()
          out_df['bearish_kicking']=self.bearish_kicking()
          out_df['bearish_meeting_lines']=self.bearish_meeting_lines()
          out_df['bearish_separating_lines']=self.bearish_separating_lines()
          out_df['bearish_side_by_side_white_lines']=self.bearish_side_by_side_white_lines()
          out_df['bearish_three_line_strike']=self.bearish_three_line_strike()
          out_df['bearish_tri_star']=self.bearish_tri_star()
          out_df['bullish_belt_hold']=self.bullish_belt_hold()
          out_df['bullish_breakaway']=self.bullish_breakaway()
          out_df['bullish_doji_star']=self.bullish_doji_star()
          out_df['bullish_engulfing']=self.bullish_engulfing()
          out_df['bullish_harami']=self.bullish_harami()
          out_df['bullish_harami_cross']=self.bullish_harami_cross()
          out_df['bullish_kicking']=self.bullish_kicking()
          out_df['bullish_meeting_lines']=self.bullish_meeting_lines()
          out_df['bullish_separating_lines']=self.bullish_separating_lines()
          out_df['bullish_side_by_side_white_lines']=self.bullish_side_by_side_white_lines()
          out_df['bullish_three_line_strike']=self.bullish_three_line_strike()
          out_df['bullish_tri_star']=self.bullish_tri_star()
          out_df['collapsing_doji_star']=self.collapsing_doji_star()
          out_df['conceling_baby_swallow']=self.conceling_baby_swallow()
          out_df['dark_cloud_cover']=self.dark_cloud_cover()
          out_df['deliberation']=self.deliberation()
          out_df['gapping_down_doji']=self.gapping_down_doji()
          out_df['gapping_up_doji']=self.gapping_up_doji()
          out_df['northern_doji']=self.northern_doji()
          out_df['southern_doji']=self.southern_doji()
          out_df['bearish_doji_star']=self.bearish_doji_star()
          out_df['bullish_doji_star']=self.bullish_doji_star()
          out_df['evening_doji']=self.evening_doji()
          out_df['downside_gap_three_methods']=self.downside_gap_three_methods()
          out_df['downside_tasuki_gap']=self.downside_tasuki_gap()
          out_df['falling_three_methods']=self.falling_three_methods()
          out_df['falling_window']=self.falling_window()
          out_df['hammer']=self.hammer()
          out_df['inverted_hammer']=self.inverted_hammer()
          out_df['hanging_man']=self.hanging_man()
          out_df['high_wave']=self.high_wave()
          out_df['homing_pigeon']=self.homing_pigeon()
          out_df['identical_three_crows']=self.identical_three_crows()
          out_df['in_neck']=self.in_neck()
          out_df['ladder_bottom']=self.ladder_bottom()
          out_df['last_engulfing_bottom']=self.last_engulfing_bottom()
          out_df['last_engulfing_top']=self.last_engulfing_top()
          out_df['matching_low']=self.matching_low()
          out_df['mat_hold']=self.mat_hold()
          out_df['morning_doji_star']=self.morning_doji_star()
          out_df['morning_star']=self.morning_star()
          out_df['on_neck']=self.on_neck()
          out_df['piercing_pattern']=self.piercing_pattern()
          out_df['rickshaw_man']=self.rickshaw_man()
          out_df['rising_three_methods']=self.rising_three_methods()
          out_df['rising_window']=self.rising_window()
          out_df['shooting_star_1']=self.shooting_star_1()
          out_df['shooting_star_2']=self.shooting_star_2()
          out_df['stick_sandwich']=self.stick_sandwich()
          out_df['takuri_line']=self.takuri_line()
          out_df['three_black_crows']=self.three_black_crows()
          out_df['three_inside_down']=self.three_inside_down()
          out_df['three_inside_up']=self.three_inside_up()
          out_df['three_outside_down']=self.three_outside_down()
          out_df['three_outside_up']=self.three_outside_up()
          out_df['three_stars_in_south']=self.three_stars_in_south()
          out_df['three_white_soldiers']=self.three_white_soldiers()
          out_df['thrusting']=self.thrusting()
          out_df['tweezers_bottom']=self.tweezers_bottom()
          out_df['tweezers_top']=self.tweezers_top()
          out_df['two_black_gapping']=self.two_black_gapping()
          out_df['two_crows']=self.two_crows()
          out_df['unique_three_river_bottom']=self.unique_three_river_bottom()
          out_df['upside_gap_three_methods']=self.upside_gap_three_methods()
          out_df['upside_gap_two_crows']=self.upside_gap_two_crows()
          out_df['upside_tasuki_gap']=self.upside_tasuki_gap()

          return out_df


    def doji(self,data_pt):

        if float(max(data_pt['Close'], data_pt['Open']))/float(min(data_pt['Close'], data_pt['Open'])) < 1.001:
            return True
        else:
            return False


    def dragonfly_doji(self,data_pt):
        '''
        Look for a long lower shadow with a small body
        (open and close are within pennies of each other).
        '''
        a = self.doji(data_pt)
        b = ((data_pt['Close']-data_pt['Low'])/data_pt['Close']) > 0.03
        c = self.similar_price(data_pt['Open'], data_pt['High'])
        if a and b and c:
            return True
        else:
            return False


    def gravestone_doji(self,data_pt):
        '''
        Look for a candle with a tall upper shadow and little or no lower one.
        The opening and closing prices should be within pennies of each other.
        '''
        a = self.doji(data_pt)
        b = ((data_pt['High']-data_pt['Open'])/data_pt['Open']) > 0.03
        c = self.similar_price(data_pt['Open'], data_pt['Low'])
        if a and b and c:
            return True
        else:
            return False

    def long_legged_doji(self,data_pt):
        '''
        Look for a doji (opening and closing prices are within a few pennies of each other) accompanied by long shadows.
        '''
        a = self.doji(data_pt)
        b = ((data_pt['High']-data_pt['Open'])/data_pt['Open']) > 0.03
        c = ((data_pt['Close']-data_pt['Low'])/data_pt['Close']) > 0.03
        if a and b and c:
            return True
        else:
            return False

    def body_candle(self,data_pt):
        return abs(data_pt['Close'] - data_pt['Open'])

    def black_candle(self,data_pt):
        if (data_pt['Close'] > data_pt['Open']) and (not self.doji(data_pt)):
            return False
        else:
            return True

    def tall_black_candle(self,data_pt):
        if self.black_candle(data_pt) and float(data_pt['Open'])/(data_pt['Close']) > 1.02:
            return True
        else:
            return False

    def small_black_candle(self,data_pt):
        if self.black_candle(data_pt) and (not self.tall_black_candle(data_pt)):
            return True
        else:
            return False

    def white_candle(self,data_pt):
        if (data_pt['Close'] > data_pt['Open']) and (not self.doji(data_pt)):
            return True
        else:
            return False

    def tall_white_candle(self,data_pt):
        if self.black_candle(data_pt) and float(data_pt['Close'])/(data_pt['Open']) > 1.02:
            return True
        else:
            return False

    def small_white_candle(self,data_pt):
        if self.white_candle(data_pt) and not self.tall_white_candle(data_pt):
            return True
        else:
            return False

    def white_marubozu_candle(self,data_pt):
        if self.white_candle(data_pt) and (data_pt['Open'] == data_pt['Low']) and (data_pt['Close'] == data_pt['High']):
            return True
        else:
            return False

    def black_marubozu_candle(self,data_pt):
        if self.black_candle(data_pt) and (data_pt['Open'] == data_pt['High']) and (data_pt['Close'] == data_pt['Low']):
            return True
        else:
            return False

    def closing_black_marubozu_candle(self,data_pt):
        '''
        Look for a tall black candle with an upper shadow but no lower one.
        '''
        if self.tall_black_candle(data_pt) and (data_pt['Open'] != data_pt['High']) and (data_pt['Close'] == data_pt['Low']):
            return True
        else:
            return False

    def closing_white_marubozu_candle(self,data_pt):
        '''
        Look for a tall white candle with an lower shadow but no upper one.
        '''
        if self.tall_white_candle(data_pt) and (data_pt['Open'] != data_pt['Low']) and (data_pt['Close'] == data_pt['High']):
            return True
        else:
            return False

    def black_spinning_top_candle(self,data_pt):
        '''
        Look for a small black body with shadows taller than the body.
        '''
        a = self.small_black_candle(data_pt)
        b = (data_pt['Close'] - data_pt['Low']) > 2 * self.body_candle(data_pt)
        c = (data_pt['High'] - data_pt['Open']) > 2 * self.body_candle(data_pt)
        if a and b and c:
            return True
        else:
            return False

    def black_spinning_top_candle(self,data_pt):
        '''
        Look for a small white bodied candle with tall shadows.
        '''
        a = self.small_white_candle(data_pt)
        b = (data_pt['Close'] - data_pt['Low']) > 2 * self.body_candle(data_pt)
        c = (data_pt['High'] - data_pt['Open']) > 2 * self.body_candle(data_pt)
        if a and b and c:
            return True
        else:
            return False

    def up_price_trend(self,data_pt, data_pt1, data_pt2):
        '''
        data_pt: the first day for the pattern
        data_pt1: the day before the pattern, last day for the upward trend
        data_pt2: the first day to compare as upward trend
        '''
        if ((data_pt1['Close'] /float(data_pt2['Open'])) > 1.03):
            return True
        else:
            return False

    def down_price_trend(self,data_pt, data_pt1, data_pt2):
        '''
        data_pt: the first day for the pattern
        data_pt1: the day before the pattern, last day for the upward trend
        data_pt2: the first day to compare as upward trend
        '''
        if ((float(data_pt2['Open']/data_pt1['Close'])) > 1.03):
            return True
        else:
            return False

    def similar_price(self,data_pt1,data_pt2, percent = 0.001):
        a = (abs(data_pt1 - data_pt2)/(data_pt2)) < percent
        if a :
            return True
        else:
            return False

    def eight_new_price(self):
        for i in xrange(1,9):
            if not (self.data.iloc[-i]['High'] > self.data.iloc[-i-1]['High']):
                return False
        if self.data.iloc[-9]['High'] < self.data.iloc[-10]['High']:
            return True
        else:
            return False

    def ten_new_price(self):
        for i in xrange(1,11):
            if not (self.data.iloc[-i]['High'] > self.data.iloc[-i-1]['High']):
                return False
        if self.data.iloc[-11]['High'] < self.data.iloc[-12]['High']:
            return True
        else:
            return False

    def twelve_new_price(self):
        for i in xrange(1,13):
            if not (self.data.iloc[-i]['High'] > self.data.iloc[-i-1]['High']):
                return False
        if self.data.iloc[-13]['High'] < self.data.iloc[-14]['High']:
            return True
        else:
            return False

    def thirteen_new_price(self):
        for i in xrange(1,14):
            if not (self.data.iloc[-i]['High'] > self.data.iloc[-i-1]['High']):
                return False
        if self.data.iloc[-14]['High'] < self.data.iloc[-15]['High']:
            return True
        else:
            return False

    def bearish_abandoned_baby(self):
        a = self.data.iloc[-1]['Close'] < self.data.iloc[-1]['Open']
        b = float(self.data.iloc[-1]['Open'])/(self.data.iloc[-1]['Close']) > 1.02
        c = self.data.iloc[-1]['High'] < self.data.iloc[-2]['Low']
        d = float(max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']))/float(min(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open'])) < 1.001
        e = self.data.iloc[-2]['Low'] > self.data.iloc[-3]['High']
        f = float(self.data.iloc[-3]['Close'])/(self.data.iloc[-3]['Open']) > 1.02
        g = self.up_price_trend(self.data.iloc[-3],self.data.iloc[-4], self.data.iloc[-6])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False
        # if self.data.iloc[-1]['Close'] < self.data.iloc[-1]['Open']:
        #     if float(self.data.iloc[-1]['Open'])/(self.data.iloc[-1]['Close']) > 1.03:
        #         if self.data.iloc[-1]['High'] < self.data.iloc[-2]['Low']:
        #             if float(max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']))/float(min(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open'])) < 1.01:
        #                 if self.data.iloc[-2]['Low'] > self.data.iloc[-3]['High']:
        #                     if float(self.data.iloc[-3]['Close'])/(self.data.iloc[-3]['Open']) > 1.03:

    def bullish_abandoned_baby(self):
        a = self.data.iloc[-1]['Close'] > self.data.iloc[-1]['Open']
        b = float(self.data.iloc[-1]['Close'])/(self.data.iloc[-1]['Open']) > 1.02
        c = self.data.iloc[-1]['Low'] > self.data.iloc[-2]['High']
        d = float(max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']))/float(min(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open'])) < 1.001
        e = self.data.iloc[-2]['High'] < self.data.iloc[-3]['Low']
        f = float(self.data.iloc[-3]['Open'])/(self.data.iloc[-3]['Close']) > 1.02
        g = self.down_price_trend(self.data.iloc[-3],self.data.iloc[-4], self.data.iloc[-6])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def above_stomach(self):
        a = self.data.iloc[-2]['Close'] < self.data.iloc[-2]['Open']
        b = self.data.iloc[-2]['Open']/float(self.data.iloc[-2]['Close']) > 1.02
        c = (self.data.iloc[-1]['Close'] > self.data.iloc[-1]['Open']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Open'])
        d = self.data.iloc[-1]['Close']/float(self.data.iloc[-1]['Open']) > 1.02
        e = self.data.iloc[-1]['Open'] > ((float(self.data.iloc[-2]['Open'])+self.data.iloc[-2]['Close'])/2)
        f = self.data.iloc[-2]['Open'] > self.data.iloc[-1]['Open']
        g = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d and e and g:
            return True
        else:
            return False

    def advance_block(self):
        a = self.white_candle(self.data.iloc[-1])
        b = self.white_candle(self.data.iloc[-2])
        c = self.white_candle(self.data.iloc[-3])
        day1_body = self.data.iloc[-3]['Close']/float(self.data.iloc[-3]['Open'])
        day2_body = self.data.iloc[-2]['Close']/float(self.data.iloc[-2]['Open'])
        day3_body = self.data.iloc[-1]['Close']/float(self.data.iloc[-1]['Open'])
        d = day1_body > 1.03
        e = (day2_body > 1.005) and ( day2_body < day1_body)
        f = (day3_body > 1.005) and ( day3_body < day1_body)
        g = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open'])
        h = (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Open'])
        j = (self.data.iloc[-1]['High'] - self.data.iloc[-1]['Close']) > (self.data.iloc[-1]['Close'] - self.data.iloc[-1]['Open'])
        k = (self.data.iloc[-2]['High'] - self.data.iloc[-2]['Close']) > (self.data.iloc[-2]['Close'] - self.data.iloc[-2]['Open'])
        l = self.up_price_trend(self.data.iloc[-3],self.data.iloc[-4], self.data.iloc[-6])
        if a and b and c and d and e and f and g and h and j and k and l:
            return True
        else:
            return False

    def below_stomach(self):
        '''
        Look for a tall white candle followed by a candle that has a body below the middle of the white candle.
        The second candle as black, but the guidelines I saw did not mentions this as a requirement.
        '''
        a = self.black_candle(self.data.iloc[-1])
        b = self.white_candle(self.data.iloc[-2])
        c = self.data.iloc[-1]['Open']/float(self.data.iloc[-1]['Close']) > 1.02
        d = self.data.iloc[-2]['Close']/float(self.data.iloc[-2]['Open']) > 1.02
        e = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] < (float(self.data.iloc[-2]['Open'])+self.data.iloc[-2]['Close'])/2)
        f = self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open']
        g = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def bearish_belt_hold(self):
        '''
        Price opens at the high for the day and closes near the low, forming a tall black candle, often with a small lower shadow.
        '''
        a = self.tall_black_candle(self.data.iloc[-1])
        b = (self.data.iloc[-1]['Close']/float(self.data.iloc[-1]['Low']) < 1.01) and (self.data.iloc[-1]['Close'] < float(self.data.iloc[-1]['Low']))
        c = (self.data.iloc[-1]['Open'] ==  self.data.iloc[-1]['High'])
        d = self.white_candle(self.data.iloc[-2])
        e = self.up_price_trend(self.data.iloc[-1],self.data.iloc[-2], self.data.iloc[-4])
        if a and b and c and d and e:
            return True
        else:
            return False

    def bearish_breakaway(self):
        '''
        Look for 5 candle lines in an upward price trend with the first candle being a tall white one.
        The second day should be a white candle with a gap between the two bodies, but the shadows can overlap.
        Day three should have a higher close and the candle can be any color.
        Day 4 shows a white candle with a higher close.
        The last day is a tall black candle with a close within the gap between the bodies of the first two candles.
        '''
        a = self.tall_white_candle(self.data.iloc[-5])
        b = self.white_candle(self.data.iloc[-4])
        c = self.data.iloc[-4]['Open'] > self.data.iloc[-5]['Close']
        d = self.data.iloc[-3]['Close'] > self.data.iloc[-4]['Close']
        e = self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Close']
        f = self.white_candle(self.data.iloc[-2])
        g = self.tall_black_candle(self.data.iloc[-1])
        h = (self.data.iloc[-1]['Close'] < self.data.iloc[-4]['Open']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-5]['Close'])
        i = self.up_price_trend(self.data.iloc[-5],self.data.iloc[-6], self.data.iloc[-8])
        if a and b and c and d and e and f and g and h and i:
            return True
        else:
            return False

    def bearish_doji_star(self):
        '''
        Look for a two-candle pattern in an uptrend.
        The first candle is a long white one.
        The next day, price gaps higher and the body remains above the prior body.
        A doji forms with the opening and closing prices within pennies of each other.
        The shadows on the doji should be comparatively short.
        '''
        a = self.tall_white_candle(self.data.iloc[-2])
        b = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close'])
        c = self.doji(self.data.iloc[-1])
        d = (self.data.iloc[-1]['High'] - self.data.iloc[-1]['Low']) < self.body_candle(self.data.iloc[-2])
        e = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d and e:
            return True
        else:
            return False

    def bearish_engulfing(self):
        '''
        Look for a two candle pattern in an upward price trend.
        The first candle is white and the second is black.
        The body of the black candle is taller and overlaps the candle of the white body.
        Shadows are unimportant.
        '''
        a = self.white_candle(self.data.iloc[-2])
        b = self.black_candle(self.data.iloc[-1])
        c = (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close'])
        d = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d:
            return True
        else:
            return False

    def bearish_harami(self):
        '''
        Look for a tall white candle followed by a small black one.
        The opening and closing prices must be within the body of the white candle.
        Ignore the shadows.
        Either the tops of the bodies or the bottoms (or both) must be a different price.
        '''
        a = self.tall_white_candle(self.data.iloc[-2])
        b = (self.black_candle(self.data.iloc[-1])) and (not self.tall_black_candle(self.data.iloc[-1]))
        c = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Open'])
        d = (self.data.iloc[-1]['High'] != self.data.iloc[-2]['High']) or (self.data.iloc[-1]['Low'] != self.data.iloc[-2]['Low'])
        e = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d:
            return True
        else:
            return False

    def bearish_harami_cross(self):
        '''
        Look for a tall white candle in an upward price trend.
        The next day, a doji appears that is inside (including the shadows) the trading range of the white candle.
        '''
        a = self.tall_white_candle(self.data.iloc[-2])
        b = self.doji(self.data.iloc[-1])
        c = (self.data.iloc[-1]['High'] < self.data.iloc[-2]['High']) and (self.data.iloc[-1]['Low'] > self.data.iloc[-2]['Low'])
        d = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        if a and b and c and d:
            return True
        else:
            return False

    def bearish_kicking(self):
        '''
        The first days is a white marubozu candle followed by a black marubozu. Between the two candles must be a gap.
        '''
        a = self.white_marubozu_candle(self.data.iloc[-2])
        b = self.black_marubozu_candle(self.data.iloc[-1])
        c = self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']
        if a and b and c:
            return True
        else:
            return False

    def bearish_meeting_lines(self):
        '''
        Look for a tall white candle in an upward price trend.
        Following that, the next candle should be a tall black one.
        The closes of the two candles should be "near" one another, whatever that means.
        '''
        a = self.up_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_white_candle(self.data.iloc[-2])
        c = self.tall_black_candle(self.data.iloc[-1])
        d = (abs(self.data.iloc[-1]['Close'] - self.data.iloc[-2]['Close'])/(self.data.iloc[-1]['Close'])) < 0.001
        if a and b and c and d:
            return True
        else:
            return False

    def bearish_separating_lines(self):
        '''
        Look for a tall white candle in a downward price trend followed by a tall black candle.
        The opening price of the two candles should be similar.
        '''
        a = self.down_price_trend(self.data.iloc[-2],self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_white_candle(self.data.iloc[-2])
        c = self.tall_black_candle(self.data.iloc[-1])
        d = (abs(self.data.iloc[-1]['Open'] - self.data.iloc[-2]['Open'])/(self.data.iloc[-1]['Open'])) < 0.001
        if a and b and c and d:
            return True
        else:
            return False

    def bearish_side_by_side_white_lines(self):
        '''
        Look for a black candle in a downward price trend.
        Following that, find two white candles with bodies about the same size and similar opening prices.
        The closing prices of both white candles must remain below the body of the black candle.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.black_candle(self.data.iloc[-3])
        c = self.white_candle(self.data.iloc[-2])
        d = self.white_candle(self.data.iloc[-1])
        e = self.similar_price(self.data.iloc[-2]['Close'],self.data.iloc[-1]['Close'])
        f = self.similar_price(self.data.iloc[-2]['Open'],self.data.iloc[-1]['Open'])
        g = self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Close']
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def bearish_three_line_strike(self):
        '''
        Look for three black candles forming lower lows followed by a tall white candle that
        opens below the prior close and closes above the first day's open.
        In other words, the last candle spans most of the price action of the prior three days.
        '''
        a = self.down_price_trend(self.data.iloc[-4], self.data.iloc[-5], self.data.iloc[-7])
        b = self.black_candle(self.data.iloc[-2])
        c = self.black_candle(self.data.iloc[-3])
        d = self.black_candle(self.data.iloc[-4])
        e = (self.data.iloc[-2]['Low'] < self.data.iloc[-3]['Low']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Close'])
        f = (self.data.iloc[-3]['Low'] < self.data.iloc[-4]['Low']) and (self.data.iloc[-3]['Close'] < self.data.iloc[-4]['Close'])
        g = self.tall_white_candle(self.data.iloc[-1])
        h = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-4]['Open'])

        if a and b and c and d and e and f and g and h:
            return True
        else:
            return False

    def bearish_tri_star(self):
        '''
        Look for three doji candles, the middle one has a body above the other two.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.doji(self.data.iloc[-3])
        c = self.doji(self.data.iloc[-2])
        d = self.doji(self.data.iloc[-1])
        e = min(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']) > max(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open'])
        f = min(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']) > max(self.data.iloc[-3]['Close'], self.data.iloc[-3]['Open'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def bullish_belt_hold(self):
        '''
        Look for a white candle with no lower shadow, but closing near the high.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.white_candle(self.data.iloc[-1])
        c = self.data.iloc[-1]['Low'] == self.data.iloc[-1]['Open']
        d = self.similar_price(self.data.iloc[-1]['High'], self.data.iloc[-1]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_breakaway(self):
        '''
        Look for a series of five candles in a downtrend.
        The first candle is tall and black followed by another black one that opens lower,
        leaving a gap between the two bodies (but shadows can overlap).
        The third day is a candle of any color but it should have a lower close.
        Day four is a black candle with a lower close.
        The final day is a tall white candle that closes within the body gap of the first two candles.
        '''
        a = self.down_price_trend(self.data.iloc[-5],self.data.iloc[-6], self.data.iloc[-8])
        b = self.tall_black_candle(self.data.iloc[-5])
        c = (self.black_candle(self.data.iloc[-4])) and (self.data.iloc[-4]['Open'] < self.data.iloc[-5]['Close'])
        d = self.data.iloc[-3]['Close'] < self.data.iloc[-4]['Close']
        e = (self.black_candle(self.data.iloc[-2])) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Close'])
        f = self.tall_white_candle(self.data.iloc[-1])
        g = (self.data.iloc[-1]['Close'] > self.data.iloc[-4]['Open']) and (self.data.iloc[-1]['Close'] < self.data.iloc[-5]['Close'])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def bullish_doji_star(self):
        '''
        Look for a tall black candle on the first day followed by a doji
        (where the opening and closing prices are within pennies of each other)
        that gaps below the prior candle's body.
        The shadows can overlap, but the doji's shadows should not be unusually long, whatever that means.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = (self.tall_black_candle(self.data.iloc[-2])) and self.doji(self.data.iloc[-1])
        c = max(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open']) < self.data.iloc[-2]['Close']
        d = (self.data.iloc[-1]['High']-self.data.iloc[-1]['Low']) < self.body_candle(self.data.iloc[-2])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_engulfing(self):
        '''
        Look for two candles in a downward price trend.
        The first is a black candle followed by a taller white one.
        The white candle should have a close above the prior open and an open below the prior close.
        In other words, the body of the white candle should engulf or overlap the body of the black candle.
        Ignore the shadows.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.black_candle(self.data.iloc[-2])
        c = self.tall_white_candle(self.data.iloc[-1])
        d = (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_harami(self):
        '''
        Look for a tall black candle in a downward price trend.
        The next day a white candle should be nestled within the body of the prior candle.
        Ignore the shadows. The tops or bottoms of the bodies can be the same price, but not both.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.white_candle(self.data.iloc[1])
        d = (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_harami_cross(self):
        '''
        Look for a two candle pattern in a downward price trend.
        The first line is a tall black candle followed by a doji that fits within the high-low price range of the prior day.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.doji(self.data.iloc[-1])
        d = (self.data.iloc[-1]['High'] < self.data.iloc[-2]['High']) and (self.data.iloc[-1]['Low'] < self.data.iloc[-2]['Low'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_kicking(self):
        '''
        Look for a tall black marubozu candle followed by an upward gap then a tall white marubozu candle.
        '''
        a = self.tall_black_candle(self.data.iloc[-2])
        b = self.black_marubozu_candle(self.data.iloc[-2])
        c = self.tall_white_candle(self.data.iloc[-1])
        d = self.white_marubozu_candle(self.data.iloc[-1])
        e = self.data.iloc[-1]['Low'] > self.data.iloc[-2]['High']
        if a and b and c and d and e:
            return True
        else:
            return False

    def bullish_meeting_lines(self):
        '''
        Look for a tall black candle followed by a tall white candle in an upward price trend.
        The two closes should be near one another.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.tall_white_candle(self.data.iloc[-1])
        d = self.similar_price(self.data.iloc[-1]['Close'], self.data.iloc[-2]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_separating_lines(self):
        '''
        Look for a tall black candle in an upward price trend followed by a tall white candle.
        The two candles share a common opening price.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.tall_white_candle(self.data.iloc[-1])
        d = self.similar_price(self.data.iloc[-1]['Open'], self.data.iloc[-2]['Open'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_side_by_side_white_lines(self):
        '''
        Look for three white candles in an upward price trend.
        The last two candles should have bodies of similar size,
        open near the same price and above the top of the body of the first white candle.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.white_candle(self.data.iloc[-1]) and self.white_candle(self.data.iloc[-2]) and self.white_candle(self.data.iloc[-3])
        c = (self.similar_price(self.data.iloc[-1]['Open'], self.data.iloc[-2]['Open'])) and (self.similar_price(self.data.iloc[-1]['Close'], self.data.iloc[-2]['Close']))
        d = (self.data.iloc[-1]['Open'] > self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_three_line_strike(self):
        '''
        Look for three white candles each with a higher close.
        A tall black candle should open higher, but close below the open of the first candle.
        '''
        a = self.up_price_trend(self.data.iloc[-4], self.data.iloc[-5], self.data.iloc[-7])
        b = (self.white_candle(self.data.iloc[-4])) and (self.white_candle(self.data.iloc[-3])) and (self.white_candle(self.data.iloc[-2]))
        c = (self.data.iloc[-4]['Close'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Close'])
        d = self.tall_black_candle(self.data.iloc[-1])
        e = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] < self.data.iloc[-4]['Open'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def bullish_tri_star(self):
        '''
        Look for three doji after a downward price trend.
        The middle doji has a body below the other two.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = (self.doji(self.data.iloc[-3])) and (self.doji(self.data.iloc[-2])) and (self.doji(self.data.iloc[-1]))
        c = max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']) < min(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open'])
        d = max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']) < min(self.data.iloc[-3]['Close'], self.data.iloc[-3]['Open'])
        if a and b and c and d:
            return True
        else:
            return False

    def collapsing_doji_star(self):
        '''
        Look for a white candle in an upward price trend.
        Following that, find a doji that gaps below yesterday's low.
        The last day is a black candle that also gaps below the doji.
        None of the shadows on the three candles should overlap, so there should be gaps surrounding the doji.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.white_candle(self.data.iloc[-3])
        c = (self.doji(self.data.iloc[-2])) and (self.data.iloc[-2]['High'] < self.data.iloc[-3]['Low'])
        d = (self.black_candle(self.data.iloc[-1])) and (self.data.iloc[-1]['High'] < self.data.iloc[-2]['Low'])
        if a and b and c and d:
            return True
        else:
            return False

    def conceling_baby_swallow(self):
        '''
        Look for four black candles.
        The first two are long black marubozu candles followed the next day by a candle with a tall upper shadow.
        The candle gaps open downward but price trades into the body of the prior day.
        The last candle engulfs the prior day, including the shadows (a higher high and lower low than the prior day).
        '''
        a = self.down_price_trend(self.data.iloc[-4], self.data.iloc[-5], self.data.iloc[-7])
        b = (self.tall_black_candle(self.data.iloc[-4])) and (self.black_marubozu_candle(self.data.iloc[-4]))
        c = (self.tall_black_candle(self.data.iloc[-3])) and (self.black_marubozu_candle(self.data.iloc[-3]))
        d = self.black_candle(self.data.iloc[-2]) and ((self.data.iloc[-2]['High'] - self.data.iloc[-2]['Open']) > self.body_candle(self.data.iloc[-2]))
        e = (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['High'] > self.data.iloc[-3]['Close'])
        f = (self.data.iloc[-1]['High'] < self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Low'] > self.data.iloc[-2]['Close'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def dark_cloud_cover(self):
        '''
        Look for two candles in an upward price trend.
        The first candle is a tall white one followed by a black candle with an opening price above the top of the white candle
        (an opening price above the prior high), but a close below the mid point of the white body.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_white_candle(self.data.iloc[-2])
        c = (self.black_candle(self.data.iloc[-1])) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['High'])
        d = (self.data.iloc[-1]['Close'] < (self.data.iloc[-2]['Open'] + self.data.iloc[-2]['Close'])/2.)
        if a and b and c and d:
            return True
        else:
            return False

    def deliberation(self):
        '''
        Look for three white candlesticks in an upward price trend.
        The first two are tall bodied candles but the third has a small body that opens near the second day's close.
        Each candle opens and closes higher than the previous one.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3]) and self.tall_white_candle(self.data.iloc[-2])
        c = self.white_candle(self.data.iloc[-1]) and (not self.tall_white_candle(self.data.iloc[-1]))
        d = self.similar_price(self.data.iloc[-1]['Open'], self.data.iloc[-2]['Close'])
        e = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open']) and (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Open'])
        f = (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Close'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def gapping_down_doji(self):
        '''
        In a downtrend, price gaps lower and forms a doji
        (a candle in which the opening and closing prices are no more than a few pennies apart).
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.doji(self.data.iloc[-1])
        c = self.data.iloc[-1]['High'] < self.data.iloc[-2]['Low']
        if a and b and c:
            return True
        else:
            return False

    def gapping_up_doji(self):
        '''
        Price gaps higher, including the shadows, in an uptrend and forms a doji candle.
        A doji is one in which the opening and closing prices are within pennies of each other.
        '''
        a = self.up_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.doji(self.data.iloc[-1])
        c = self.data.iloc[-1]['Low'] > self.data.iloc[-2]['High']
        if a and b and c:
            return True
        else:
            return False

    def northern_doji(self):
        '''
        Look for a candle in which the opening and closing prices are within pennies of each other (a doji) in an up trend.
        '''
        a = self.up_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.doji(self.data.iloc[-1])
        if a and b:
            return True
        else:
            return False

    def southern_doji(self):
        '''
        Look for a doji candlestick (one in which the opening and closing prices are a few pennies from each other) in a downward price trend.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.doji(self.data.iloc[-1])
        if a and b:
            return True
        else:
            return False

    def bearish_doji_star(self):
        '''
        Look for a two-candle pattern in an uptrend.
        The first candle is a long white one.
        The next day, price gaps higher and the body remains above the prior body.
        A doji forms with the opening and closing prices within pennies of each other.
        The shadows on the doji should be comparatively short.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_white_candle(self.data.iloc[-2])
        c = self.doji(self.data.iloc[-1]) and (not self.dragonfly_doji(self.data.iloc[-1])) and (not self.gravestone_doji(self.data.iloc[-1])) and (not self.long_legged_doji(self.data.iloc[-1]))
        d = min(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']) > self.data.iloc[-1]['Close']
        if a and b and c and d:
            return True
        else:
            return False

    def bullish_doji_star(self):
        '''
        Look for a tall black candle on the first day followed by a doji
        (where the opening and closing prices are within pennies of each other)
        that gaps below the prior candle's body.
        The shadows can overlap, but the doji's shadows should not be unusually long, whatever that means.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.doji(self.data.iloc[-1]) and (not self.dragonfly_doji(self.data.iloc[-1])) and (not self.gravestone_doji(self.data.iloc[-1])) and (not self.long_legged_doji(self.data.iloc[-1]))
        d = max(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']) < self.data.iloc[-1]['Close']
        if a and b and c and d:
            return True
        else:
            return False

    def evening_doji(self):
        '''
        Look for a tall white candle in an upward price trend followed by a doji whose body gaps above the two surrounding days.
        Ignore the shadows. The last day is a tall black candle that closes at or below the mid point of the first day.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3])
        c = self.doji(self.data.iloc[-2])
        d = (min(self.data.iloc[-2]['Open'],self.data.iloc[-2]['Close']) > self.data.iloc[-3]['Close']) and (min(self.data.iloc[-2]['Open'],self.data.iloc[-2]['Close']) > self.data.iloc[-1]['Open'])
        e = self.tall_black_candle(self.data.iloc[-1])
        f = self.data.iloc[-1]['Close'] <= (self.data.iloc[-3]['Close'] + self.data.iloc[-3]['Open'])/2.
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def downside_gap_three_methods(self):
        '''
        Look for two long black bodied candles in a downward price trend.
        The second candle should have a gap between them (shadows do not overlap).
        The last day is a white candle that opens within the body of the prior day and
        closes within the body of the first day, closing the gap between the two black candles.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.black_candle(self.data.iloc[-3]) and self.black_candle(self.data.iloc[-2])
        c = self.data.iloc[-3]['Low'] > self.data.iloc[-2]['High']
        d = self.white_candle(self.data.iloc[-1])
        e = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Open'])and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close'])
        f = (self.data.iloc[-1]['Close'] < self.data.iloc[-3]['Open'])and (self.data.iloc[-1]['Close'] > self.data.iloc[-3]['Close'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def downside_tasuki_gap(self):
        '''
        Look for a black candle in a downward price trend followed by another black candle,
        but this one gaps lower with no shadow overlap between the two candles.
        The final day sees a white candle print on the chart,
        one that opens within the body of the second candle and closes within the gap between the first and second candles.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.black_candle(self.data.iloc[-3]) and self.black_candle(self.data.iloc[-2])
        c = self.data.iloc[-3]['Low'] > self.data.iloc[-2]['High']
        d = self.white_candle(self.data.iloc[-1])
        e = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Open'])
        f = (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['High']) and (self.data.iloc[-1]['Close'] < self.data.iloc[-3]['Low'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def falling_three_methods(self):
        '''
        Look for a series of five candles in a downward price trend.
        The first day should be a tall black candle followed by three up trending small white candles
        (except the middle of the three, which can be either black or white),
        followed by another tall black candle with a close below the first day's close.
        The three middle candles should remain within the high-low range of the first candle.
        '''
        a = self.down_price_trend(self.data.iloc[-5], self.data.iloc[-6], self.data.iloc[-8])
        b = self.tall_black_candle(self.data.iloc[-5])
        c = self.small_white_candle(self.data.iloc[-4]) and self.small_white_candle(self.data.iloc[-2]) and (self.small_black_candle(self.data.iloc[-3]) or self.small_white_candle(self.data.iloc[-3]))
        d = self.tall_black_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] < self.data.iloc[-5]['Close'])
        e = (self.data.iloc[-4]['High'] <  self.data.iloc[-5]['High']) and (self.data.iloc[-3]['High'] <  self.data.iloc[-5]['High']) and (self.data.iloc[-2]['High'] <  self.data.iloc[-5]['High'])
        f = (self.data.iloc[-4]['Low'] >  self.data.iloc[-5]['Low']) and (self.data.iloc[-3]['Low'] >  self.data.iloc[-5]['Low']) and (self.data.iloc[-2]['Low'] >  self.data.iloc[-5]['Low'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def falling_window(self):
        '''
        Find a pattern in which yesterday's low is above today's high.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.data.iloc[-2]['Low'] > self.data.iloc[-1]['High']
        if a and b:
            return True
        else:
            return False

    def hammer(self):
        '''
        Look for the hammer to appear in a downward price trend and
        have a long lower shadow at least two or three times the height of the body with little or no upper shadow.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = (min(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']) - self.data.iloc[-1]['Low']) > 2 * self.body_candle(self.data.iloc[-1])
        c = self.similar_price(self.data.iloc[-1]['High'], max(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']))
        if a and b and c:
            return True
        else:
            return False

    def inverted_hammer(self):
        '''
        Look for a tall black candle with a close near the day's low followed by a short candle with a tall upper shadow and little or no lower shadow.
        The second candle cannot be a doji
        (opening and closing prices cannot be within pennies of each other) and
        the open on the second candle must be below the prior candle's close.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2]) and self.similar_price(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Low'])
        c = (not self.doji(self.data.iloc[-1])) and (self.small_white_candle(self.data.iloc[-1]) or self.small_black_candle(self.data.iloc[-1]))
        d = self.similar_price(self.data.iloc[-1]['Low'], min(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']))
        e = (self.data.iloc[-1]['High'] - max(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close'])) > 2 * self.body_candle(self.data.iloc[-1])
        f = self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def hanging_man(self):
        '''
        Look for a small bodied candle atop a long lower shadow in an uptrend.
        '''
        a = self.up_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.small_white_candle(self.data.iloc[-1]) or self.small_black_candle(self.data.iloc[-1])
        c = self.hammer()
        if a and b and c :
            return True
        else:
            return False

    def high_wave(self):
        '''
        Look for tall upper and lower shadows attached to a small body.
        The body is not a doji (meaning that the opening and closing prices must be more than a few pennies apart.
        '''
        a = self.small_white_candle(self.data.iloc[-1]) or self.small_black_candle(self.data.iloc[-1])
        b = not self.doji(self.data.iloc[-1])
        c = (self.data.iloc[-1]['High'] - max(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close'])) > 2 * self.body_candle(self.data.iloc[-1])
        d = (min(self.data.iloc[-1]['Open'], self.data.iloc[-1]['Close']) - self.data.iloc[-1]['Low']) > 2 * self.body_candle(self.data.iloc[-1])
        if a and b and c and d:
            return True
        else:
            return False

    def homing_pigeon(self):
        '''
        Look for a two line candle in a downward price trend.
        The first day should be a tall black body followed by a small black body that fits inside the body of the prior day.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.small_black_candle(self.data.iloc[-1])
        d = self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close']
        e = self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Open']
        if a and b and c and d and e:
            return True
        else:
            return False

    def identical_three_crows(self):
        '''
        Look for three tall black candles, the last two opening near the prior candle's close.
        Some sources require each candle to be similar in size, but this one is rare enough without that restriction.
        '''
        a = self.up_price_trend(self.data.iloc[-3],  self.data.iloc[-4], self.data.iloc[-6])
        b = (self.tall_black_candle(self.data.iloc[-3])) and (self.tall_black_candle(self.data.iloc[-2])) and (self.tall_black_candle(self.data.iloc[-1]))
        c = self.similar_price(self.data.iloc[-2]['Open'], self.data.iloc[-3]['Close']) and self.similar_price(self.data.iloc[-1]['Open'], self.data.iloc[-2]['Close'])
        if a and b and c:
            return True
        else:
            return False

    def in_neck(self):
        '''
        Look for a tall black candle in a downward price trend.
        The next day, a white candle opens below the black day's low, but closes just into the body of the black candle.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.white_candle(self.data.iloc[-1])
        d = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Low']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] < (self.data.iloc[-2]['Close']+self.data.iloc[-2]['Open'])/2.)
        if a and b and c and d:
            return True
        else:
            return False

    def ladder_bottom(self):
        '''
        Look for a series of 5 candles in a downward price trend.
        The first three days should be tall black candles, each with a lower open and close.
        The 4th day should be a black candle with an upper shadow,
        and the last day should be a white candle that gaps open above the body of the prior day.
        '''
        a = self.down_price_trend(self.data.iloc[-5], self.data.iloc[-6], self.data.iloc[-8])
        b = self.tall_black_candle(self.data.iloc[-5]) and self.tall_black_candle(self.data.iloc[-4]) and self.tall_black_candle(self.data.iloc[-3])
        c = (self.data.iloc[-4]['Close'] < self.data.iloc[-5]['Close']) and (self.data.iloc[-3]['Close'] < self.data.iloc[-4]['Close'])
        d = (self.data.iloc[-4]['Open'] < self.data.iloc[-5]['Open']) and (self.data.iloc[-3]['Open'] < self.data.iloc[-4]['Open'])
        e = self.black_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['High'] > self.data.iloc[-2]['Open'])
        f = self.white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def last_engulfing_bottom(self):
        '''
        Look for a white candle on the first day in a downward price trend followed by a black candle that engulfs the body of the white candle.
        That means the black candle has a body this is above the top and below the bottom of the white candle.
        Ignore the shadows.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.white_candle(self.data.iloc[-2]) and self.black_candle(self.data.iloc[-1])
        c = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open'])
        if a and b and c:
            return True
        else:
            return False

    def last_engulfing_top(self):
        '''
        Look for a black candle followed by a white candle that overlaps the prior black candle's body.
        The white candle should have a body above the prior candle's top and below the prior candle's bottom.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.white_candle(self.data.iloc[-1]) and self.black_candle(self.data.iloc[-2])
        c = (self.data.iloc[-2]['Low'] > self.data.iloc[-1]['Open']) and (self.data.iloc[-2]['High'] < self.data.iloc[-1]['Close'])
        if a and b and c:
            return True
        else:
            return False

    def matching_low(self):
        '''
        Look for a black candle with a tall body.
        Following that, find a black body with a close (not the low) that matches the prior close.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2]) and self.black_candle(self.data.iloc[-1])
        c = self.data.iloc[-1]['Close'] == self.data.iloc[-2]['Close']
        if a and b and c:
            return True
        else:
            return False

    def mat_hold(self):
        '''
        Look for a tall white candle to start the pattern.
        The next day a small black candle has a higher close.
        The third day can be any color but it is also a small candle.
        The fourth day is, again, a small black candle and all three candles (days 2 to 4)
        show a downward price trend but their bodies remain above the low of the first day.
        The last day is another tall white candle with a close above the high of the prior four candles.
        '''
        a = self.up_price_trend(self.data.iloc[-5], self.data.iloc[-6], self.data.iloc[-8])
        b = self.tall_white_candle(self.data.iloc[-5])
        c = self.small_black_candle(self.data.iloc[-4]) and (self.data.iloc[-4]['Close'] > self.data.iloc[-5]['Close'])
        d = self.small_black_candle(self.data.iloc[-3]) or self.small_white_candle(self.data.iloc[-3])
        e = self.small_black_candle(self.data.iloc[-2]) and self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        f = (self.data.iloc[-2]['Close'] > self.data.iloc[-5]['Low']) and (min(self.data.iloc[-3]['Close'], self.data.iloc[-3]['Open'])> self.data.iloc[-5]['Low']) \
            and (self.data.iloc[-4]['Close'] > self.data.iloc[-5]['Low'])
        g = self.tall_white_candle(self.data.iloc[-1]) and self.data.iloc[-1]['Close'] > max(self.data.iloc[-2]['High'], self.data.iloc[-3]['High'], self.data.iloc[-4]['High'], self.data.iloc[-5]['High'])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def morning_doji_star(self):
        '''
        Look for a tall black candle in a downward price trend.
        The next day, a doji appears and its body gaps below the prior candle's body.
        The final day is a tall white candle whose body gaps above the doji's.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3]) and self.doji(self.data.iloc[-2])
        c = max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']) < self.data.iloc[-3]['Close']
        d = self.tall_white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Open'] > max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']))
        if a and b and c and d:
            return True
        else:
            return False

    def morning_star(self):
        '''
        Look for a tall black candle in a downward price trend.
        Following that, a small bodied candle of any color appears, one whose body gaps below the prior body.
        The last day is a tall white candle that gaps above the body of the second candle and closes at least midway into the body of the first day.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3]) and (self.small_black_candle(self.data.iloc[-2]) or self.small_white_candle(self.data.iloc[-2]))
        c = max(self.data.iloc[-2]['Open'], self.data.iloc[-2]['Close']) < self.data.iloc[-3]['Close']
        d = self.tall_white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Open'] > max(self.data.iloc[-2]['Close'], self.data.iloc[-2]['Open']))
        if a and b and c and d:
            return True
        else:
            return False

    def on_neck(self):
        '''
        Look for a tall black candle in a downward price trend. Following that, a white candle has a close that matches (or nearly matches) the prior low.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.tall_black_candle(self.data.iloc[-2])
        c = self.white_candle(self.data.iloc[-1]) and self.similar_price(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Low'])
        if a and b and c:
            return True
        else:
            return False

    def piercing_pattern(self):
        '''
        Look for a black candle followed by a white one that opens below the black candle's low and closes between the midpoint of the black body and opening price.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.black_candle(self.data.iloc[-2]) and self.white_candle(self.data.iloc[-1])
        c = self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Low']
        d = (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Close'] > (self.data.iloc[-2]['Open'] - self.body_candle(self.data.iloc[-2])/2.))
        if a and b and c and d:
            return True
        else:
            return False

    def rickshaw_man(self):
        '''
        Look for the opening and closing prices to be within pennies of each other,
        unusually tall upper and lower shadows, and the body to be near the middle of the candlestick.
        '''
        a = self.long_legged_doji(self.data.iloc[-1])
        b = self.similar_price(self.data.iloc[-1]['Open'], (self.data.iloc[-1]['High'] + self.data.iloc[-1]['Low'])/2.) or self.similar_price(self.data.iloc[-1]['Close'], (self.data.iloc[-1]['High'] + self.data.iloc[-1]['Low'])/2.)
        if a and b:
            return True
        else:
            return False

    def rising_three_methods(self):
        '''
        Look for a tall white candle followed by three small candles that trend lower but close within the high-low range of the first candle.
        Candles 2 and 4 are black, but day 3 can be any color.
        The final candle in the pattern is a tall white one that closes above the close of the first day.
        '''
        a = self.up_price_trend(self.data.iloc[-5], self.data.iloc[-6], self.data.iloc[-8])
        b = self.tall_white_candle(self.data.iloc[-5])
        c = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        d = self.small_black_candle(self.data.iloc[-4]) and (self.data.iloc[-4]['Close'] < self.data.iloc[-5]['High']) and (self.data.iloc[-4]['Close'] > self.data.iloc[-5]['Low'])
        e = (self.small_black_candle(self.data.iloc[-3]) or self.small_white_candle(self.data.iloc[-3])) and (self.data.iloc[-3]['Close'] < self.data.iloc[-5]['High']) and (self.data.iloc[-3]['Close'] > self.data.iloc[-5]['Low'])
        f = self.small_black_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Close'] < self.data.iloc[-5]['High']) and (self.data.iloc[-2]['Close'] > self.data.iloc[-5]['Low'])
        g = self.tall_white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] > self.data.iloc[-5]['Close'])
        if a and b and c and d and e and f and g:
            return True
        else:
            return False

    def rising_window(self):
        '''
        Find a pattern in which yesterday's high is below today's low.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.data.iloc[-2]['High'] < self.data.iloc[-1]['Low']
        if a and b:
            return True
        else:
            return False

    def shooting_star_1(self):
        '''
        Look for a small bodied candle (but not a doji) with little or no lower shadow and
        a tall upper shadow at least twice the height of the body.
        '''
        a = self.up_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.small_black_candle(self.data.iloc[-1]) or self.small_white_candle(self.data.iloc[-1])
        c = self.similar_price(self.data.iloc[-1]['Low'], min(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open']))
        d = (self.data.iloc[-1]['High'] - max(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open'])) > 2 * self.body_candle(self.data.iloc[-1])
        if a and b and c and d:
            return True
        else:
            return False

    def shooting_star_2(self):
        '''
        Look for two candles in an upward price trend.
        The first candle is white followed by a small bodied candle with an upper shadow at least three times the height of the body.
        The candle has no lower shadow or a very small one and there is a gap between the prices of the two bodies.
        The second candle can be any color.
        '''
        a = self.up_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.white_candle(self.data.iloc[-2])
        c = self.small_black_candle(self.data.iloc[-1]) or self.small_white_candle(self.data.iloc[-1])
        d = (self.data.iloc[-1]['High'] - max(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open'])) > 3 * self.body_candle(self.data.iloc[-1])
        e = self.similar_price(self.data.iloc[-1]['Low'], min(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open']))
        f = self.data.iloc[-1]['Low'] > self.data.iloc[-2]['Close']
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def stick_sandwich(self):
        '''
        Look for a black candle in a falling price trend.
        The second candle is white and it trades above the close of the prior day.
        The last candle is a black one that closes at or near the close of the first day.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.black_candle(self.data.iloc[-3]) and self.white_candle(self.data.iloc[-2]) and self.black_candle(self.data.iloc[-1])
        c = (self.data.iloc[-2]['Low'] > self.data.iloc[-3]['Close'])
        d = self.similar_price(self.data.iloc[-1]['Close'], self.data.iloc[-3]['Close'])
        if a and b and c and d:
            return True
        else:
            return False

    def takuri_line(self):
        '''
        A small bodied candle with a lower shadow at least three times the height of the body and little or no upper shadow.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.small_black_candle(self.data.iloc[-1]) or self.small_white_candle(self.data.iloc[-1])
        c = self.similar_price(self.data.iloc[-1]['High'], max(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open']))
        d = abs(self.data.iloc[-1]['Low'] - min(self.data.iloc[-1]['Close'], self.data.iloc[-1]['Open'])) > 3 * self.body_candle(self.data.iloc[-1])
        if a and b and c and d:
            return True
        else:
            return False

    def three_black_crows(self):
        '''
        Look for three tall black candles that appear in an upward price trend.
        Candles 2 and 3 of the pattern should open within the body of the prior candle,
        and all three should close near their lows, making new lows along the way.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3]) and self.tall_black_candle(self.data.iloc[-2]) and self.tall_black_candle(self.data.iloc[-1])
        c = (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Open'])
        d = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Open'])
        e = self.similar_price(self.data.iloc[-3]['Low'], self.data.iloc[-3]['Close']) and self.similar_price(self.data.iloc[-2]['Low'], self.data.iloc[-2]['Close']) and self.similar_price(self.data.iloc[-1]['Low'], self.data.iloc[-1]['Close'])
        f = (self.data.iloc[-3]['Low'] > self.data.iloc[-2]['Low']) and (self.data.iloc[-2]['Low'] > self.data.iloc[-1]['Low'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def three_inside_down(self):
        '''
        Look for a tall white candle in an upward price trend.
        Following that, a small black candle appears with the open and close within the body of the first day.
        The tops or bottoms of the two bodies can be the same price, but not both.
        The last day must close lower, but can be any color.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3])
        c = self.small_black_candle(self.data.iloc[-2])
        d = (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Open'])
        e = (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Close'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def three_inside_up(self):
        '''
        Look for a tall black candle in a downward price trend.
        The next day, a small bodied white candle has a body that is within the body of the prior candle.
        The tops or bottoms of the bodies can be the same price, but not both.
        The last day is a white candle that closes above the prior close.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3])
        c = self.small_white_candle(self.data.iloc[-2])
        d = (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Open'])
        e = self.white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def three_outside_down(self):
        '''
        Look for a white candle in an upward price trend.
        Following that, a black candle opens higher and closes lower than the prior candle's body.
        The last day is a candle with a lower close.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.white_candle(self.data.iloc[-3])
        c = self.black_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Open'] > self.data.iloc[-2]['Close']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-2]['Open'])
        d = self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Close']
        if a and b and c and d:
            return True
        else:
            return False

    def three_outside_up(self):
        '''
        Look for a black candle in a downward price trend.
        Following that, a white candle opens below the prior body and closes above it, too.
        The last day is a candle in which price closes higher, according to Morris who developed the candle.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.black_candle(self.data.iloc[-3])
        c = self.white_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Open'])
        d = self.data.iloc[-1]['Close'] > self.data.iloc[-2]['Close']
        if a and b and c and d:
            return True
        else:
            return False

    def three_stars_in_south(self):
        '''
        Look for a tall black candle with a long lower shadow to appear in a downward price trend.
        The second day should be similar to the first day, but smaller and with a higher low.
        The last day is a black marubozu that squeezes inside the high-low range of the prior day.
        Good luck finding one.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3]) and ((self.data.iloc[-3]['Close']-self.data.iloc[-3]['Low']) > self.body_candle(self.data.iloc[-3]))
        c = self.tall_black_candle(self.data.iloc[-2]) and ((self.data.iloc[-2]['Close']-self.data.iloc[-2]['Low']) > self.body_candle(self.data.iloc[-2]))
        d = self.data.iloc[-2]['Low'] > self.data.iloc[-3]['Low']
        e = self.black_marubozu_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['High'] < self.data.iloc[-2]['High']) and (self.data.iloc[-1]['Low'] > self.data.iloc[-2]['Low'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def three_white_soldiers(self):
        '''
        Look for three tall white candles, each with a close near the high, higher closes, and
        bodies that overlap (an opening price within the prior candle's body.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3]) and self.tall_white_candle(self.data.iloc[-2]) and self.tall_white_candle(self.data.iloc[-1])
        c = self.similar_price(self.data.iloc[-3]['High'], self.data.iloc[-3]['Close']) and self.similar_price(self.data.iloc[-2]['High'], self.data.iloc[-2]['Close']) and self.similar_price(self.data.iloc[-1]['High'], self.data.iloc[-1]['Close'])
        d = (self.data.iloc[-3]['High'] < self.data.iloc[-2]['High']) and (self.data.iloc[-2]['High'] < self.data.iloc[-1]['High'])
        e = (self.data.iloc[-2]['Open'] > self.data.iloc[-3]['Open']) and (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Close'])
        f = (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close'])
        if a and b and c and d and e and f:
            return True
        else:
            return False

    def thrusting(self):
        '''
        Look for a black candle in a downward price trend followed by a white candle that
        opens below the prior low but closes near but below the midpoint of the black candle's body.
        '''
        a = self.down_price_trend(self.data.iloc[-2], self.data.iloc[-3], self.data.iloc[-5])
        b = self.black_candle(self.data.iloc[-2]) and self.white_candle(self.data.iloc[-1])
        c = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Low']) and (self.data.iloc[-1]['Close'] < (self.data.iloc[-2]['Open'] - self.body_candle(self.data.iloc[-2])/2.)) and \
            (self.data.iloc[-1]['Close'] > (self.data.iloc[-2]['Close'] + self.body_candle(self.data.iloc[-2])/4.))
        if a and b and c:
            return True
        else:
            return False

    def tweezers_bottom(self):
        '''
        Look for two candles sharing the same low price.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.data.iloc[-1]['Low'] == self.data.iloc[-2]['Low']
        if a and b:
            return True
        else:
            return False

    def tweezers_top(self):
        '''
        Look for two adjacent candlesticks with the same (or nearly the same) high price in an uptrend.
        '''
        a = self.up_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.similar_price(self.data.iloc[-1]['High'], self.data.iloc[-2]['High'])
        if a and b:
            return True
        else:
            return False

    def two_black_gapping(self):
        '''
        Look for a price gap followed by two black candles.
        The second black candle should have a high below the prior candle's high.
        '''
        a = self.down_price_trend(self.data.iloc[-1], self.data.iloc[-2], self.data.iloc[-4])
        b = self.black_candle(self.data.iloc[-2]) and self.black_candle(self.data.iloc[-1])
        c = self.data.iloc[-2]['High'] < self.data.iloc[-3]['Low']
        d = self.data.iloc[-1]['High'] < self.data.iloc[-2]['High']
        if a and b and c and d:
            return True
        else:
            return False

    def two_crows(self):
        '''
        Look for a tall white candle in an upward price trend.
        Following that, a black candle has a body that gaps above the prior candle's body.
        The last day is another black candle, but this one opens within the prior candle's body and closes within the body of the first candle in the pattern.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3])
        c = self.black_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Close'])
        d = self.black_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Close'])
        e = (self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Open']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Close'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def unique_three_river_bottom(self):
        '''
        Look for a tall bodied black candle in a downward price trend.
        Following that, another black body rests inside the prior body, but the lower shadow is below the prior day's low.
        The last day is a short bodied white candle that remains below the body of the prior candle.
        '''
        a = self.down_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_black_candle(self.data.iloc[-3])
        c = self.black_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Low'] < self.data.iloc[-3]['Low'])
        d = (self.data.iloc[-2]['Open'] < self.data.iloc[-3]['Open']) and (self.data.iloc[-2]['Close'] < self.data.iloc[-3]['Close'])
        e = self.small_white_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Close'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def upside_gap_three_methods(self):
        '''
        Look for two tall white candles in an upward price trend.
        There should be a gap between them, including between the shadows.
        The last day is a black candle that fills the gap created by the first two days.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3]) and self.tall_white_candle(self.data.iloc[-2])
        c = self.data.iloc[-3]['High'] < self.data.iloc[-2]['Low']
        d = self.black_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] < self.data.iloc[-3]['Close']) and (self.data.iloc[-1]['Close'] > self.data.iloc[-3]['Open'])
        e = (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open'])
        if a and b and c and d and e:
            return True
        else:
            return False

    def upside_gap_two_crows(self):
        '''
        Look for a tall white candle in an upward price trend.
        Then find a black candle with a body gapping above the prior candle's body.
        The last day is another black candle that engulfs the body of the middle day with a close that
        remains above the close of the first candle.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.tall_white_candle(self.data.iloc[-3])
        c = self.black_candle(self.data.iloc[-2]) and (self.data.iloc[-3]['Close'] < self.data.iloc[-2]['Close'])
        d = self.black_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Close']) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open'])
        e = self.data.iloc[-2]['Close'] > self.data.iloc[-3]['Close']
        if a and b and c and d and e:
            return True
        else:
            return False

    def upside_tasuki_gap(self):
        '''
        Look for a white candle in an upward price trend.
        Following that, find another white candle, but this one gaps higher and that includes a gap between the shadows of the two candles.
        The last day is a black candle that opens in the body of the prior candle and closes within the gap created between the first two candles.
        '''
        a = self.up_price_trend(self.data.iloc[-3], self.data.iloc[-4], self.data.iloc[-6])
        b = self.white_candle(self.data.iloc[-3])
        c = self.white_candle(self.data.iloc[-2]) and (self.data.iloc[-2]['Low'] > self.data.iloc[-3]['High'])
        d = self.black_candle(self.data.iloc[-1]) and (self.data.iloc[-1]['Open'] > self.data.iloc[-2]['Open']) and (self.data.iloc[-1]['Open'] < self.data.iloc[-2]['Close'])
        e = (self.data.iloc[-1]['Close'] > self.data.iloc[-3]['Close']) and (self.data.iloc[-1]['Close'] < self.data.iloc[-2]['Open'])
        if a and b and c and d and e:
            return True
        else:
            return False
