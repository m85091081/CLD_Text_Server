# -*- coding: utf-8 -*-
import hashlib
from flask import session, request, render_template, Blueprint, url_for, redirect
from database import User

main = Blueprint('main', __name__ , template_folder='../template')
# index page main route page 
@main.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template('index.html', **locals())
    else:
        return render_template('login.html')

# init route to first time use
@main.route('/init', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        user = request.form['buser']
        passd = request.form['bpass']
        hashsha = hashlib.sha256(passd.replace('\n', '').encode())
        User.add(user, hashsha.hexdigest(), '1')

        return redirect(url_for('main.index'))
    else:
        return render_template('first.html')
