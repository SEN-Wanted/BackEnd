# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, jsonify
import json
from sqlalchemy import distinct
from . import convert_to_json_string, db

store_by_id = Blueprint('store_by_id', __name__)

@store_by_id.route('/index/<storeID>', methods=['GET', 'POST'])
def store_info(storeID):
    '''
    SZQ
    获取单个电铺点单信息，返回定义的json化数据
    '''
    stores_by_id = Store.query.filter_by(id=storeID).first()
    if stores_by_id is None:
        return jsonify({'status_code': '401', 'error_message': 'StoreID Not Exist'})
    dishes_by_type = db.session.query(Dishes.title).filter_by(storeId=storeID).distinct().all()
    if dishes_by_type is None:
        return jsonify({'status_code': '401', 'error_message': 'Dishes Not Exist'})
    print convert_to_json_string(dishes_by_type)
    dishes_type_dict = json.loads(convert_to_json_string(dishes_by_type), encoding='utf-8')
    foodData = []
    count = 0
    for type in dishes_type_dict:
        count = count + 1
        foodDataList = {}
        foodDataList['title']=type[0]
        foodDataList['id'] = count
        foodDataList['data']=[]
        dishes_by_type = Dishes.query.filter_by(id=storeID,title=type).all()
        dishes_by_type_dict = json.loads(convert_to_json_string(dishes_by_type))
        for dish_by_type in dishes_by_type_dict:
            dish_by_type_dict = {}
            dish_by_type_dict['name']=dish_by_type['dishName']
            dish_by_type_dict['monthlySale'] = dish_by_type['monthlySale']
            dish_by_type_dict['price'] = dish_by_type['dishPrice']
            dish_by_type_dict['icon'] = dish_by_type['img']
            foodDataList['data'].append(dish_by_type_dict)
        foodData.append(foodDataList)
    return jsonify({'status_code': '200','foodData':foodData})
