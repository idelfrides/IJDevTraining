#!usr/bin/env python3
# -*- coding: utf-8 -*-




"""

Unit Testing in Action

Now, we will explore unit testing in action. For our example, we will be testing a function that gets stock data from Yahoo Finance using pandas_datareader and do this in PyUnit:

"""

import pytest
from datetime import datetime
import pandas as pd

import pandas_datareader.data as web



def get_stock_data(ticker):
    """### pull data from stooq """

    return web.DataReader(ticker, 'yahoo')


# scope="class" tears down the fixture only at the end of the last test in the class, so we avoid rerunning this step.

@pytest.fixture(scope='class')
def stock_df():
    """### We only want to pull this data once for each TestCase since it is an expensive operation"""
    return get_stock_data('^DJI')


class TestGetStockData():

    def test_column_present(self, stock_df):
        """### Ensures that the expected columns are all present"""

        assert 'Open'   in  stock_df.columns
        assert 'High'   in  stock_df.columns
        assert 'Low'    in  stock_df.columns
        assert 'Close'  in  stock_df.columns
        assert 'Volume' in  stock_df.columns


    def test_non_empty(self, stock_df):
        """### Ensures that there is mone than one row of data"""
        assert len(stock_df.index) != 0

    '''
    def test_high_low(self, stock_df):
        """### Ensure high and low are the highest and lowest in the same row"""
        ohlc = self.df[['Open', 'High', 'Low', 'Close', 'Volume']]

        highest = ohlc.max(axis=1)
        lowest = ohlc.min(axis=1)
        self.assertTrue(ohlc.le(highest, axis=0).all(axis=None))
        self.assertTrue(ohlc.ge(lowest, axis=0).all(axis=None))
    '''

    def test_most_recent_within_week(self, stock_df):
        """### Most recent data was collected within the last week"""

        most_recent_date = pd.to_datetime(stock_df.index[-1])
        assert (datetime.today() - most_recent_date).days <= 7
