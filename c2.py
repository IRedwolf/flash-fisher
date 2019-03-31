#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-31 下午1:43
# @Author  : Tingfeng
# @Site    : 
# @File    : c2.py
# @Software: PyCharm
from contextlib import contextmanager

@contextmanager
def book_mark():
	print('<',end='')
	yield
	print('>',end='')
	
with book_mark():
	print('切克闹',end='')