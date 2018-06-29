# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, g
from . import auth
from .models import *

user_login = Blueprint('user_login', __name__)

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

@user_login.route('/login', methods=['GET', 'POST'])
def sign():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if verify_password(username, password):
            # 号码以及密码验证通过
            pass
        else:
            # 手机号或者密码错误
            error = jsonify({'status_code':'401','error_message':'Unauthorized'})
            return error
        # user = User.query.filter_by(phone=username).first()
        token = g.user.generate_auth_token(6000)
        status_code = "201"
        user_data = {
            'status_code': status_code,
            'token': token,
            'duration': 6000,
            "user": {
                "id": g.user.id,
                "phone": g.user.phone,
                "nickname": g.user.nickname,
                "avar": '/static/images/user_img/test_user_1.png',
                "message": '这个人很懒什么都没留下',
                "orderList": []
            }
        }
        json_user_data = jsonify(user_data)
        return json_user_data
    else:
        error = jsonify({'status_code': '400', 'error_message': 'INVALID REQUEST'})
        return error

