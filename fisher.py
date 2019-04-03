#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-15 下午10:12
# @Author  : Tingfeng
# @Site    : 
# @File    : d_2.py
# @Software: PyCharm

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8899)
