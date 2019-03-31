#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-15 下午10:41
# @Author  : Tingfeng
# @Site    : 
# @File    : httper.py
# @Software: PyCharm

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
