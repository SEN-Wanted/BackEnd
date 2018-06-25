# -*- coding: UTF-8 -*-
from .models import *
from flask import Blueprint, jsonify
import json

store_by_id = Blueprint('store_by_id', __name__)

@store_by_id.route('/index/<storeID>', methods=['GET', 'POST'])
def store_info(storeID):
    '''
    SZQ
    获取单个电铺点单信息，返回定义的json化数据
    '''
    store_list = ['110', '111']
    storeID_exist = True
    for id_index in store_list:
        print id_index
        if (storeID == id_index):
            storeID_exist = True
            break
        else:
            storeID_exist = False

    if (storeID_exist):
        print storeID
        path = './json_test/' + storeID + '.json'
        try:
            print path
            json_fd = open(path, 'r')
        except IOError:
            print "fault"
            return jsonify({'status_code':'401','error_message':'OrderData File Not Found'})
    else:
        return jsonify({'status_code':'401','error_message':'StoreID Not Exist'})

    json_fd_dict = json.load(json_fd)
    # 使用flask中定义返回的json而不是content：html.text
    # json_fd_str = json.dumps(json_fd_dict, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    json_fd_data = jsonify(json_fd_dict)
    return json_fd_data
