# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, jsonify
import hashlib
from app import db
from .models import Order, Dishes, Store

order_info = Blueprint('order', __name__)

@order_info.route('/user/<userID>/orders/<orderID>', methods=['GET', 'POST'])
def order_info_detail(userID, orderID):
    '''
    SXT
    订单详情api
    用户身份和订单信息确认后输出订单详细信息,失败返回（401）
    '''

    if request.method == 'GET':
        if vaild_order(userID, orderID):
            for per_user_order in Order.query.filter_by(username = userID):
            # per_user_order = Order.query.filter_by(username = userID).first()
            # print per_user_order.dishesId
            # dishes = Dishes.query.filter_by(id = per_user_order.dishesId).first()
                for dishes in Dishes.query.filter_by(id = per_user_order.dishesId):
                    print dishes.id
                    store_name = Store.query.filter_by(id = dishes.storeId).first().storeName
                    listFood = [{
                        "icon": "none",
                        "dishName": dishes.dishName,
                        "storeid": dishes.storeId,
                        # "starRating": 4.4,
                        "price": dishes.dishPrice,
                        "monthlySell": dishes.monthlySale,
                        # "distance": 418,
                        # "isDiscount": false,
                        # "DiscountNumber": 0,
                        # "isAppOffer": true
                    }]
                    status_code = '201'
                    order_hash = hashlib.md5(orderID)
                    order_detail = {
                        'status_code': status_code,
                        'storeName': store_name,
                        'foodList': listFood,
                        # 'mealFee': '123',
                        # 'ServiceFee': '123',
                        'totalFee': per_user_order.totalPrice,
                        # 'Offer': '123',
                        # 'paymentMethod': '1',
                        'Date': per_user_order.createTime,
                        'orderNumber': order_hash.hexdigest()
                    }
                    json_order_data = jsonify(order_detail)
                    return json_order_data
        else:
            return 'fall'
        # token = request.headers['accesstoken']
        # user = User.verify_auth_token(token)
        # if not user:
        #     return jsonify({'status_code': '401', 'error_message': 'Unauthorized'})
        # else:
        #     path = './json_test/' + userID + '_detail_' + orderID + '_order.json'
        #     try:
        #         print path
        #         json_od = open(path, 'r')
        #     except IOError:
        #         print "fault"
        #         return jsonify({'status_code': '401', 'error_message': 'OrderData File Not Found'})
        #     json_od_dict = json.load(json_od)
        #     json_order_data = jsonify(json_od_dict)
        #     return json_order_data

def vaild_order(userID, OrderID):
    if userID is None or OrderID is None:
        return False
    if Order.query.filter_by(username= userID).first() is None:
        return False
    return True