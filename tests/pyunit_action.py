#!usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Unit Testing in Action

Now, we will explore unit testing in action. For our example, we will be testing a function that gets stock data from Yahoo Finance using pandas_datareader and do this in PyUnit:

"""

import unittest
from datetime import datetime
import pandas as pd

import pandas_datareader.data as web


def get_stock_data(ticker):
    """### pull data from stooq """

    return web.DataReader(ticker, 'yahoo')
    # return df


class TestGetStockData(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """### We only want to pull this data once for each TestCase since it is an expensive operation"""
        self.df = get_stock_data('^DJI')

        print(self.df.info())
        print(self.df)


    def test_column_present(self):
        """### Ensures that the expected columns are all present"""

        self.assertIn('Open', self.df.columns)
        self.assertIn('High', self.df.columns)
        self.assertIn('Low', self.df.columns)
        self.assertIn('Close', self.df.columns)
        self.assertIn('Volume', self.df.columns)


    def test_non_empty(self):
        """### Ensures that there is mone than one row of data"""
        self.assertNotEqual(len(self.df.index), 0)


    def test_high_low(self):
        """### Ensure high and low are the highest and lowest in the same row"""
        ohlc = self.df[['Open', 'High', 'Low', 'Close', 'Volume']]

        highest = ohlc.max(axis=1)
        lowest = ohlc.min(axis=1)
        self.assertTrue(ohlc.le(highest, axis=0).all(axis=None))
        self.assertTrue(ohlc.ge(lowest, axis=0).all(axis=None))


    def test_most_recent_within_week(self):
        """### Most recent data was collected within the last week"""
        most_recent_date = pd.to_datetime(self.df.index[-1])
        self.assertLessEqual((datetime.today() - most_recent_date).days, 7)



if __name__ == '__main__':
    unittest.main()
