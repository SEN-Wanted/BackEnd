# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, g
from . import db, auth
from .models import User
import hashlib
user_info = Blueprint('user',__name__)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(phone=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@user_info.route('/sign_up', methods=['GET', 'POST'])
def sign():
    '''
    SXT
    注册api,创建用户，并将用户的信息存入数据库
    在数据库中查找手机号，存在则非法，返回失败信息（401）
    餐馆图像存储在'/static/images/user_img/'目录下
    message和orderlist为空
    '''
    username = request.form.get('username')
    password = request.form.get('password')
    if valid_sign_up(username, password):
        # default user
        user1 = User(phone=username, password_hash = password, payPassword = password, money = 0, isAdmin = 0)
        user1.hash_password(password)
        db.session.add(user1)
        db.session.commit()
    else:
        error = jsonify({'status_code': '401', 'error_message': 'Unauthorized'})
        return error
    verify_password(username, password)
    token = g.user.generate_auth_token(6000)
    status_code = "201"
    user_data = {
       'status_code': status_code,
       'token': token,
       'duration': 6000,
       "user": {
           "id": user1.id,
           "phone": user1.phone,
           "nickname": user1.nickname,
           "avar": '/static/images/user_img/test_user_1.png',
           "message": '这个人很懒什么都没留下',
           "orderList": []
        }
    }
    json_user_data = jsonify(user_data)
    return json_user_data

def valid_sign_up(username, password):
    if username is None or password is None:
        return False
    if User.query.filter_by(phone=username).first() is not None:
        return False
    return True