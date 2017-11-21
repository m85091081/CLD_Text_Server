# -*- coding: utf-8 -*-

import hashlib
from flask import session, redirect, url_for, request, Blueprint
from database import User

auth = Blueprint('auth', __name__ , template_folder='../template')
@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['buser']
        passd = request.form['bpass']
        password = User.login(user)
        passd = hashlib.sha256(passd.replace('\n', '').encode()).hexdigest()
        if not password:
            return '帳號錯誤'
        else:
            if password == passd:
                session['username'] = user
                session['name'] = user
                return redirect(url_for('main.index'))
            else:
                return '密碼錯誤'

    else:
        return redirect(url_for('main.index'))


@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main.index'))

