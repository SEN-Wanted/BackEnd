# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, jsonify
import hashlib
from . import db
from .models import Order, Dishes, Store, User, food_list

order_info = Blueprint('order', __name__)

@order_info.route('/user/<userID>/orders/<orderID>', methods=['GET', 'POST'])
def order_info_detail(userID, orderID):
    '''
    SXT
    订单详情api
    用户身份和订单信息确认后输出订单详细信息,失败返回（401）
    '''
#    token = request.headers['accesstoken']
#    user = User.verify_auth_token(token)
#    if not user:
#        return jsonify({'status_code': '403', 'error_message': 'Forbidden'})

    rating = request.form.get('rating')
    
    # test initial
    rating = 1

    listFood = []
    if request.method == 'GET':
        if vaild_order(userID, orderID):
            for per_user_order in food_list.query.filter_by(orderID = orderID):
                Food_detail = {
                    'dishName': per_user_order.dishName,
                    'price': per_user_order.price,
                    'number': per_user_order.number
                }
                listFood.append(Food_detail)
            print listFood
            if listFood == []:
                return jsonify({'status_code': '401', 'error_message': 'No Order'})
            else:
                status_code = '201'
                order_hash = hashlib.md5(orderID)
                user_order = Order.query.filter_by(id = orderID).first()
                user_order.rating = rating
                db.session.commit()

                order_detail = {
                    'status_code': status_code,
                    'storeName': user_order.storeName,
                    'foodList': listFood,
                    'mealFee': user_order.mealFee,
                    'ServiceFee': user_order.ServiceFee,
                    'totalFee': user_order.totalPrice,
                    'Offer': 'undefined',
                    'paymentMethod': user_order.paymengtMethod,
                    'Date': user_order.createTime,
                    'orderNumber': order_hash.hexdigest(),
                    'rating' : user_order.rating
                }
                json_order_data = jsonify(order_detail)
                return json_order_data
        else:
            return jsonify({'status_code': '401', 'error_message': 'No User'})

def vaild_order(userID, OrderID):
    if userID is None or OrderID is None:
        return False
    if Order.query.filter_by(username= userID).first() is None:
        return False
    return True
