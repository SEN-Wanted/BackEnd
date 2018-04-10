# -*- coding: UTF-8 -*-

from flask import Flask, render_template
from flask_cors import CORS

APP = Flask(__name__)

CORS(APP)


@APP.route("/")
def home():
    '''
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return render_template('index.html')


@APP.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'


if __name__ == '__main__':
    # 开启 debug模式
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    # 把自己的电脑作为服务器，可以让别人访问
    APP.run(debug=True, host='0.0.0.0')
