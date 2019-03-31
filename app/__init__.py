#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-16 下午12:44
# @Author  : Tingfeng
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
	app = Flask(__name__)
	app.config.from_object('app.secure')
	app.config.from_object('app.setting')
	register_blueprint(app)
	
	login_manager.init_app(app)
	login_manager.login_view = 'web.login'
	login_manager.login_message = '请先登录或者注册'
	db.init_app(app)
	db.create_all(app=app)
	return app


def register_blueprint(app):
	from app.web.book import web
	app.register_blueprint(web)
