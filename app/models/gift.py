#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-20 下午5:38
# @Author  : Tingfeng
# @Site    : 
# @File    : gift.py
# @Software: PyCharm

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Gift(Base):
	__tablename__ = 'gift'
	id = Column(Integer, primary_key=True)
	uid = Column(Integer, ForeignKey('user.id'), nullable=False)
	user = relationship('User')
	isbn = Column(String(13))
	launched = Column(Boolean, default=False)
