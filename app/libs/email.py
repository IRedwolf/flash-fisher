#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tingeng
@file: email.py
@time: 2019/04/03
"""
from threading import Thread
from flask import current_app, render_template, app
from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='2078449839@qq.com', body='Test',
    #               recipients=['qq2078449839@sina.com'])
    # mail.send(msg)
    msg = Message('[鱼书]' + '' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
