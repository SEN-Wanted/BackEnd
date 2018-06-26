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
        return jsonify({'status_code':'200', 'ListStoreData':convert_to_json_string(stores)})
