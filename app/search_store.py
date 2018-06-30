# -*- coding: UTF-8 -*-
import json
from .models import *
from flask import Blueprint, request, jsonify
from . import convert_to_json_string
search_store = Blueprint('search_store', __name__)

@search_store.route("/search")
def search():
    '''
    SZQ
    返回搜索店铺分类属性下的所有店铺
    带参数传入/search?type=dessert
    '''
    key_word = request.args.get('keyword')
    type = request.args.get('type')
    if type is None and key_word is None:
        return jsonify({'status_code': '400', 'error_message': 'INVALID REQUEST'})
    if key_word is None:
        stores = Store.query.filter_by(title=type).all()
    else:
        stores = Store.query.filter(Store.storeName.like('%' + key_word + '%')).all()
        print convert_to_json_string(stores)
    if stores is None:
        return jsonify({'status_code': '400', 'error_message': 'No Stores'})
    else:
        ListStoreData = []
        stores_str=convert_to_json_string(stores)
        stores_dict = json.loads(stores_str)
        for store in stores_dict:
            s_dict = {}
            s_dict['icon']='/static/image/store_img/'+ store['img']
            s_dict['storeName']=store['storeName']
            s_dict['storeid']=store['id']
            s_dict['starRating']=store['rating']
            s_dict['price']=store['price']
            s_dict['monthlySale']=store['monthlySale']
            s_dict['distance']=store['distance']
            s_dict['isDiscount']=store['isDiscount']
            s_dict['discountNumber']=store['discountNumber']
            s_dict['isAppOffer']=store['isAppOffer']
            ListStoreData.append(s_dict)
        return jsonify({'status_code':'200', 'ListStoreData':ListStoreData})