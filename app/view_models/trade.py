#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tingeng
@file: trade.py
@time: 2019/04/{DAY}
"""


class TradeInfo():
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strfime('%Y-%m-%d'),
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            id=single.id
        )
