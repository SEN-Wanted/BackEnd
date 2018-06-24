# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, jsonify
from app import db
from .models import Store

store_info = Blueprint('store',__name__)

@store_info.route('/index', methods=['GET'])
def send_store():
    '''
    SXT
    店铺信息api，
    餐馆图像存储在'/static/images/store_img/'目录下
    和前端沟通过后JSON数据返回忽略顺序
    '''
    store_info1 = Store.query.filter_by(id = '1').first()
    store_data = {
        'icon': '/static/images/store_img/store_id' + store_info1.id + '/store.png',
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
    json_store_data = jsonify(store_data)
    return json_store_data
