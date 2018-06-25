# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, request, jsonify
import json

type_search = Blueprint('type_search', __name__)

@type_search.route("/search")
def search():
    '''
    SZQ
    返回搜索店铺分类属性下的所有店铺
    带参数传入/search?type=dessert
    '''
    type = request.args.get('type')
    path = 'json_test/' + type + '.json'
    try:
        print path
        json_fd = open(path, 'r')
    except IOError:
        return jsonify({'status_code': '401', 'error_message': '404 Not Found'})
        # return "{'status_code':'401','error_message':'404 Not Found'}"
    json_store = json.load(json_fd)
    # json_store_str = json.dumps(json_store, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    return jsonify(json_store)