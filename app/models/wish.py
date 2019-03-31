#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-31 上午11:26
# @Author  : Tingfeng
# @Site    : 
# @File    : wish.py
# @Software: PyCharm


from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship


class Wish(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	# book = relationship('Book')
	# bid = Column(Integer,ForeignKey('book.id'))
	launched = Column(Boolean, default=False)
	extend_existing = True
