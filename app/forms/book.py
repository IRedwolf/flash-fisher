#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-16 下午3:52
# @Author  : Tingfeng
# @Site    : 
# @File    : book.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
