# -*- coding: UTF-8 -*-
import json
from .models import *
from flask import Blueprint, request, jsonify
from . import convert_to_json_string
type_search = Blueprint('type_search', __name__)

@type_search.route("/search")
def search():
    '''
    SZQ
    返回搜索店铺分类属性下的所有店铺
    带参数传入/search?type=dessert
    '''
    type = request.args.get('type')
    stores = Store.query.filter_by(title=type).all()
    if type is None or stores is None:
        error = jsonify({'status_code': '400', 'error_message': 'INVALID REQUEST'})
        return error
    else:
        ListStoreData = []
        stores_str=convert_to_json_string(stores)
        stores_dict = json.loads(stores_str)
        for store in stores_dict:
            s_dict = {}
            s_dict['icon']=store['img']
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