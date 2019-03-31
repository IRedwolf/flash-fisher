#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-15 下午10:35
# @Author  : Tingfeng
# @Site    : 
# @File    : helper.py
# @Software: PyCharm

'''
 isbn isbn13 13个0-9数字
 isbn10 10个0到9 含'-'
'''


def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
