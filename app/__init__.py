from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode='utf8')
auth = HTTPBasicAuth()

from . import models,views,store_info,user_info,order_info,user_login,type_search
