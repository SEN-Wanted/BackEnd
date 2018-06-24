# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, jsonify
from app import db
from .models import User

user_info = Blueprint('user',__name__)

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

    ## test initial
    username = '13719335348'
    password = '12345678'
    
    user_info1 = User.query.filter_by(id = username).first()
    print user_info1

    if valid_sign_up(username, password):
        # default user
        user1 = User(id = username, password = password, payPassword = password, money = 0, isAdmin = 0)
        db.session.add(user1)
        db.session.commit()
    else:
        error = jsonify({'status_code': '401', 'error_message': 'Unauthorized'})
        return error

    # verify_password(username, password)
    # token = g.user.generate_auth_token(600)

    status_code = "201"
    user_data = {
       'status_code': status_code,
       'token': 'nooooop',
       'duration': 600,
       "user": {
           "ID": user1.id,
           "username": user1.id,
           "name": user1.nickname,
           "avar": '/static/images/user_img/test_user_1.png',
           "message": '这个人很懒什么都没留下',
           "orderList": []
        }
    }
    json_user_data = jsonify(user_data)
    return json_user_data
    return 'success'

def valid_sign_up(username, password):
    if username is None or password is None:
        return False
    if User.query.filter_by(id=username).first() is not None:
        return False
    return True

