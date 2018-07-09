#  SEN-Wanted Server
SEN-Wanted订餐app服务端
  
## 安装  
1.安装`python2.7`  
2.为保证系统安全，建议安装虚拟环境  

```
pip install virtualenv
```

3.新建虚拟环境  

```
virtualenv venv
```

4.激活虚拟环境  

```
source venv/bin/activate       # Linux 下
venv\scripts\activate          # Windows 下
```

5.在项目目录下，安装第三方需求包  

```
pip install -r requirements
```

## 运行  
**项目结构如下：**

```
Appserver/
├── app
│   ├── static/      # 静态资源文件夹
│   ├── templates/   # 模板文件夹
│   ├── __init__.py  # 初始化文件
│   ├── store_info.py # blueprint
│   ├── user_info.py # blueprint
│   ├── order_info.py # blueprint
│   ├── store_by_id.py # blueprint
│   ├── orders_by_user_id.py # blueprint
│   ├── type_search.py # blueprint
│   ├── user_login.py # blueprint
│   ├── models.py # 数据格式
│   └── view.py # 调用blueprint
├── config.py    # 配置文件
├── createdb.py # 创建数据库
├── client.py # 用户配置文件
├── run.py # 主程序文件
├── requirements     # 需求文件
└── README.md
```

1.切换到主程序目录  

```
cd Flask-Server/
```

2.运行项目  

```
python run.py
```

**注意：**在运行项目之前需在config.py中配置数据库相关参数

```
SQLALCHEMY_DATABASE_URI = 数据库链接
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

3.管理系统  
运行项目之后访问 [http://0.0.0.0:5000](http://localhost:5000) 可以查看API

## API
![](app/static/image/doc_img/url_list.png)
