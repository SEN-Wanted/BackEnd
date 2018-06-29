#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask,render_template,jsonify,request,g, url_for,abort
from flask_cors import CORS
from . import auth
from models import *
import hashlib
from store_info import store_info
from user_info import user_info
from order_info import order_info

from user_login import user_login
from search_store import search_store
from store_by_id import store_by_id
from orders_by_user_id import orders_by_user_id
from user_info_modify import user_info_modify
# extensions

app.register_blueprint(store_info)
app.register_blueprint(user_info)
app.register_blueprint(order_info)

app.register_blueprint(user_login)
app.register_blueprint(search_store)
app.register_blueprint(store_by_id)
app.register_blueprint(orders_by_user_id)
app.register_blueprint(user_info_modify)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(id=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})
@app.route('/api/users/<username>')
def get_user(username):
    user = User.query.filter_by(id=username).first()
    if not user:
        abort(400)
    return jsonify({'username': user.username})
@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })


@app.route("/")
def home():
    '''
    页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '餐馆信息 : /index 注册信息 : /sign_up 订单详情 : /user/<userID>/orders/<orderID> 登陆信息 : /login 单个店铺点单信息 : host/index/store_name'
    '''
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'
