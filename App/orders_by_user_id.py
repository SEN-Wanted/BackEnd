# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, request, jsonify
import json

orders_by_user_id = Blueprint('orders_by_user_id', __name__)

@orders_by_user_id.route('/user/<userID>/orders', methods=['GET', 'POST'])
def order_info_brief(userID):
    '''
    SZQ
    订单详情api
    用户身份和订单信息确认后输出订单详细信息,失败返回（401）
    '''
    token = request.headers['accesstoken']
    user = User.verify_auth_token(token)
    if not user:
        return jsonify({'status_code': '401', 'error_message': 'Unauthorized'})
    if request.method == 'GET':
        path = './json_test/' + userID + '_brief_order.json'
        try:
            print path
            json_od = open(path, 'r')
        except IOError:
            print "fault"
            return jsonify({'status_code': '401', 'error_message': 'OrderData File Not Found'})
        json_od_dict = json.load(json_od)
        json_order_data = jsonify(json_od_dict)
        return json_order_data
    if request.method == 'POST':
        path = './json_test/' + userID + '_brief_order.json'
        new_order = request.get_data()
        json_od = open(path, 'r')
        print new_order
        new_order = jsonify(new_order)

        return new_order