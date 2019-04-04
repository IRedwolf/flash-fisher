#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-15 下午8:08
# @Author  : Tingfeng
# @Site    : 
# @File    : secure.py
# @Software: PyCharm

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher1?charset=utf8'
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'adasdada@qq.com'
MAIL_PASSWORD = 'sezbfmrfsqwceiab'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'