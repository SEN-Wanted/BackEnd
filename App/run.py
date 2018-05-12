# -*- coding: UTF-8 -*-

from flask import Flask, render_template
from flask_cors import CORS
from flask import jsonify 
from flask import request
import json

APP = Flask(__name__)

CORS(APP)


@APP.route("/")
def Home():
    '''
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return '餐馆信息 : /index 注册信息 : /login 登陆信息 : /login_up 单个店铺点单信息 : host/index/store_name'


@APP.route('/index',methods=['GET'])
def SendStore():
    '''
    SXT
    这里接入数据库
    餐馆图像存储在'/static/images/store_img/'目录下
    和前端沟通过后JSON数据返回忽略顺序
    '''
    store_data = {
                    'icon': '/static/images/store_img/sm_pic',
                    'storeName': '',
                    'starRating': '',
                    'price': '',
                    'monthlySell': '',
                    'distance': '',
                    'isDiscount': '',
                    'DiscountNumber': '',
                    'isAppOffer' :'' 
    }
    json_store_data = json.dumps(store_data, ensure_ascii = False, indent = 4, sort_keys=True, separators=(',', ': '))
    return json_store_data


@APP.route('/login',methods=['GET', 'POST'])
def Login():
    form = request.form
    mobile = form.get('phone_num', '')
    password = form.get('password', '')

    '''
    SXT
    在数据库中查找手机号，存在则非法，返回失败信息
    手机号合法和密码合法性前端完成
    '''
        #查找数据库,手机号无效
        # if User.query.get(mobile) is not None:
        #     return "{'status_code':'401','error_message':'Unauthorized'}"

        #存入数据库
        # user = User()
        # user.id = mobile
        # user.password = MD5(password)
        # user.payPassword = MD5(pay_password)
        # db.session.add(user)
        # db.session.commit()
        # login_user(user, True)
    #如果成功
    #json_user_data = json.dumps(form, ensure_ascii = False, indent = 4, sort_keys=True, separators=(',', ': '))
    return "{'status_code':'201', 'user':{user info}}"



@APP.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'


if __name__ == '__main__':
    '''
    开启 debug模式
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    # 把自己的电脑作为服务器，可以让别人访问
    '''
    APP.run(debug=True, host='0.0.0.0')
