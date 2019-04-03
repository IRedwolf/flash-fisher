# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-20 下午6:52
# @Author  : Tingfeng
# @Site    : 
# @File    : auth.py
# @Software: PyCharm


from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo
from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField('password', validators=[
        DataRequired(message='密码不可以为空,请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符,最多为10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空,请输入你的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
