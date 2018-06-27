# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, g
from . import auth
from .models import *

user_info_modify = Blueprint('user_info_modify', __name__)

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

@user_info_modify.route('/users/modify', methods=['GET', 'POST'])
def sign():
    error = None
    if request.method == 'POST':
        username = request.args.get('username')
        phone_number = request.args.get('phone_number')
        old_password = request.args.get('old_password')
        new_password = request.args.get('new_password')
        if verify_password(username, old_password):
            # 号码以及密码验证通过
            user1=User.query.filter_by(phone=phone_number).first()
            user1.nickname = username
            user1.hash_password(new_password)
            db.session.commit()
        else:
            # 手机号或者密码错误
            error = jsonify({'status_code':'401','error_message':'Unauthorized'})
            return error
        token = g.user.generate_auth_token(600)
        status_code = "201"
        user_data = {
            'status_code': status_code,
            'token': token,
            'duration': 600,
            "user": {
                "ID": username,
                "username": username,
                "name": username,
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

