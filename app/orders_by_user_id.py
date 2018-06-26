# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, request, jsonify
import json

orders_by_user_id = Blueprint('orders_by_user_id', __name__)

@orders_by_user_id.route('/user/<userID>/orders', methods=['GET', 'POST'])
def order_info_brief(userID):
    '''
    SZQ
    用户订单详情
    用户身份确认后输出订单详细信息,失败返回（401）
    '''
    token = request.headers['accesstoken']
    user = User.verify_auth_token(token)
    if not user:
        return jsonify({'status_code': '401', 'error_message': 'Unauthorized'})
    if request.method == 'GET':
        json_od_dict = {
            "status_code": "201",
            "orderList": [
                {
                    "orderID": 1,
                    "storeName": "海底捞(珠影星光店)",
                    "isEvaluate": 1,
                    "evaluationGrade": 0,
                    "date": "2017-01-08 17:05:24",
                    "cost": 10
                },
                {
                    "orderID": 2,
                    "storeName": "海底捞(珠影星光店)",
                    "isEvaluate": 1,
                    "evaluationGrade": 0,
                    "date": "2017-02-08 17:05:24",
                    "cost": 10
                }
            ]
        }

        json_order_data = jsonify(json_od_dict)
        return json_order_data
    if request.method == 'POST':
        path = './json_test/' + userID + '_brief_order.json'
        new_order = request.get_data()
        json_od = open(path, 'r')
        print new_order
        new_order = jsonify(new_order)

        return new_order
