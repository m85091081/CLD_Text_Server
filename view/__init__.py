# -*- coding: utf-8 -*-
from flask import Flask
from view.index import main
from view.user import auth
from conf import setting
app = Flask(__name__)
app.secret_key = setting.yourkey
app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/login")

