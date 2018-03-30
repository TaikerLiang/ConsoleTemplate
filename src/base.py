import sys
import os
from flask import jsonify, redirect, request, url_for, render_template
from src import app
from src import db
from src.auth import auth
from src.models import users
from pprint import pprint


@app.route("/", methods=['GET'])
def hello():
    return jsonify({'err': 0, 'err_msg': 'Welcome to Flask!'})

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    login_token = request.form['login_token']

    if login_token:
        res = users.User.decode_login_auth_token(login_token)
        if isinstance(res, str):
            return jsonify({'err': -1, 'err_msg': 'Invalid token. Please log in again'})
        else:
            if res.email == email:
                api_token = (user.encode_api_auth_token()).decode("utf-8")
                res.renew_last_login_date()
                res.renew_api_token(api_token)
                return jsonify({'err': 0, 'err_msg': '', 'api_token': api_token})
            else:
                return jsonify({'err': -1, 'err_msg': 'Invalid token. Please log in again.'})

    user = users.User.query.filter_by(email=email).first()

    if user:
        pw_res = user.verify_password(password)
        if pw_res:
            login_token = (user.encode_login_auth_token()).decode("utf-8")
            api_token = (user.encode_api_auth_token()).decode("utf-8")
            user.renew_last_login_date()
            user.renew_api_token(api_token)
            res = jsonify({'err': 0, 'err_msg': '', 'login_token': login_token, 
                'api_token': api_token})
        
            return res
        else:
            return jsonify({'err': -1, 'err_msg': 'Invalid password.'})
    else:
        return jsonify({'err': -1, 'err_msg': 'Invalid email.'})


@app.route("/dashboard", methods=['GET'])
@auth.requires_auth
def dashboard():
    return jsonify({'err': 0, 'err_msg': '', 'res': 'This is dashboard'})
