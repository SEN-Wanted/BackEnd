# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, request, jsonify
from . import convert_to_json_string
from . import db
import datetime, json, hashlib

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
    if not valid_user_id(userID):
        return jsonify({'status_code': '401', 'error_message': 'No User'})
    if request.method == 'GET':
        if Order.query.filter_by(userId= userID).first() is None:
            empty_orders_tuple = []
            return jsonify({'status_code': '200', 'orderList': empty_orders_tuple})
        orders_by_user_id = Order.query.filter_by(userId= userID).all()
        orders_by_user_id_str = convert_to_json_string(orders_by_user_id)
        orders_by_user_id_dict = json.loads(orders_by_user_id_str)
        orders_tuple = []
        for order in orders_by_user_id_dict:
            orders_dict = {}
            orders_dict['orderID']=order['id']
            store = Store.query.filter_by(id=order['storeId']).first()
            orders_dict['storeIcon'] = '/static/image/store_img/'+ store.img
            orders_dict['storeName']=order['storeName']
            orders_dict['rating']=order['rating']
            orders_dict['date']=order['createTime']
            orders_dict['cost']=order['payPrice']
            orders_tuple.append(orders_dict)
        return jsonify({'status_code':'200','orderList':orders_tuple})
    if request.method == 'POST':
        order_str = request.get_data()
        if order_str is None:
            return jsonify({'status_code': '400', 'error_message': 'INVALID REQUEST'})
        order_dict = json.loads(order_str)
        foods_dict = order_dict['foodList']
        user = User.query.filter_by(id=userID).first()
        new_order = Order(userId=user.id, storeId=order_dict['storeID'], storeName=order_dict['storeName'], createTime=order_dict['date'],mealFee=order_dict['mealFee'], ServiceFee=order_dict['serviceFee'],payPrice=order_dict['totalFee']-order_dict['offer'],totalPrice=order_dict['totalFee'], paymengtMethod=order_dict['paymentMethod'])
        db.session.add(new_order)
        db.session.commit()
        for food in foods_dict:
            new_food = food_list(dishName=food['name'], number=food['number'], price=food['price'], orderID=new_order.id)
            db.session.add(new_food)
            db.session.commit()
        return jsonify({'status_code':'201'})
def valid_user_id(userID):
    if userID is None:
        return False
    if User.query.filter_by(id= userID).first() is None:
        return False
    return True