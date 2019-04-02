from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from app.view_models.wish import MyWishes
from . import web

__author__ = '七月'


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_Wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', gifts=view_model.trades)
    # pass

@login_required
@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存入你的心愿清单,请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    return 'ok'


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    return 'ok'
