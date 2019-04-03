#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tingeng
@file: enums.py
@time: 2019/04/03
"""
from enum import Enum


class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
