# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask.ext.login import (login_user, logout_user)
from mockdbhelper import MockDBHelper
from passwordhelper import PasswordHelper

app = Flask(__name__)
DB = MockDBHelper()
PH = PasswordHelper()

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password, stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

@app.route("/account")
def account():
    return "you are logged in."

if __name__ == '__main__':
    app.run(port=5000, debug=True)
