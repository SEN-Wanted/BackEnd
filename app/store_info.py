# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, jsonify
from . import db
from .models import Store

store_info = Blueprint('store',__name__)

@store_info.route('/index', methods=['GET'])
def send_store():
    '''
    SXT
    店铺信息api，
    餐馆图像存储在'/static/images/store_img/'目录下
    20180625 pro:数据库构建不完整
    '''
    store_data_temp = []
    for store_info1 in Store.query.order_by(Store.id):
        store_data1 = {
            'icon': '/static/image/store_img/' + store_info1.storeName + '/LOGO.jpg',
            'storeName': store_info1.storeName,
            'storeID': store_info1.id,
            'starRating': store_info1.rating,
            'price': '',
            'monthlySell': store_info1.ratingNum,
            'distance': store_info1.location,
            'isDiscount': store_info1.isDiscount,
            'DiscountNumber': '',
            'isAppOffer': ''
        }
        store_data_temp.append(store_data1)
    store_data = {
        'listStoreData':store_data_temp
    }
    json_store_data = jsonify(store_data)
    return json_store_data
