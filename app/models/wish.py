#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-31 上午11:26
# @Author  : Tingfeng
# @Site    : 
# @File    : wish.py
# @Software: PyCharm


from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, func, desc
from sqlalchemy.orm import relationship
from app.spider.yushu_book import YuShuBook


class Wish(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	# book = relationship('Book')
	# bid = Column(Integer,ForeignKey('book.id'))
	launched = Column(Boolean, default=False)
	extend_existing = True


	@classmethod
	def get_user_Wishes(cls, uid):
		Wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
			desc(Wish.create_time)).all()
		return Wishes

	@classmethod
	def get_gifts_counts(cls, isbn_list):
		from app.models.gift import Gift
		count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
			Gift.launched == False,
			Gift.isbn.in_(isbn_list),
			Gift.status == 1).group_by(
			Gift.isbn).all()
		count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
		return count_list

	@property
	def book(self):
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(self.isbn)
		return yushu_book.first
