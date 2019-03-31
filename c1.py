#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-31 下午12:52
# @Author  : Tingfeng
# @Site    : 
# @File    : c1.py
# @Software: PyCharm
from contextlib import contextmanager


class MyResource:
	def query(self):
		print('query data')


@contextmanager
def my_myresource():
	print('connect to resource')
	yield MyResource()
	print('close resource connect')


with my_myresource() as r:
	r.query()
