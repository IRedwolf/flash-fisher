#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tingeng
@file: trade.py
@time: 2019/04/{DAY}
"""
from app.view_models.book import BookViewModel


class TradeInfo():
    def __init__(self, trades):
        self.total = 0
        self.trades = []
        self.__parse(trades)

    def __parse(self, trades):
        self.total = len(trades)
        self.trades = [self._map_to_trade(trade) for trade in trades]

    def _map_to_trade(self, single):
        return dict(
            user_name=single.user.nickname,
            time=single.create_datetime.strftime('%Y-%m-%d'),
            id=single.id
        )


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []

        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list

        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
            return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return r
