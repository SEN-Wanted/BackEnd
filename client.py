# -*- coding: utf-8 -*-
import requests
# $5$rounds=535000$gHu.87i/yV99xMLa$RPyfo3xeuznTQpDCCHydLYYUbYyAaasVhxqPzjvF903
# data = "{'username': '111', 'password': '222'}"
data="{'storeName': '海底捞','foodList': [{'name':'鸳鸯锅底','number':1,'price':38}],'mealFee': 10,'ServiceFee' :10,'totalFee' : 10,'Offer': 10,'paymentMethod' : 1,'date':'2017-01-08 17:05:24'}"
# user_info = {'username': '15678594617', 'password': '123456'}
user_info = {'username': '13288463932', 'password': '123456'}

# user_info = {'phone': '110', 'password': '123'}
# params = {'type': 'dessert'}
token ="eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyOTg1ODE1MCwiaWF0IjoxNTI5ODU3NTUwfQ.eyJpZCI6IjEzMjg4NDYzOTMyIn0.Y0ES93n-MUjAYK1seCvwE42GepGz6ggbKn5u632rO-g"
headers = {'accesstoken':token}
# r = requests.post("http://127.0.0.1:5000/sign_up", data=user_info)
# r = requests.post("http://127.0.0.1:5000/login", data=user_info)
r = requests.post("http://127.0.0.1:5000/user/13719335341/orders", data=data, headers=headers)
# r = requests.get("http://127.0.0.1:5000/user/110/orders", headers=headers)
# r = requests.get("http://127.0.0.1:5000/api/token",auth=(user_info['username'],user_info['password']))
# r = requests.get("http://127.0.0.1:5000/api/resource",auth=(token, '222'))

# s = requests.get("http://127.0.0.1:5000/search", params=params)

print (r.text)
# print (r.cookies['phone_num'], r.cookies['password'])
# print (l.text)

# real_ip = request.headers.get('X-Real-Ip', request.remote_addr)
 # ip = request.remote_addr
 # request.headers['Authorization']
