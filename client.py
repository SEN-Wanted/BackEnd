import requests

data = "{'username': '111', 'password': '222'}"
user_info = {'username': '111', 'password': '222'}
# user_info = {'phone': '110', 'password': '123'}
# params = {'type': 'dessert'}
token ="eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyOTY3OTM4MSwiaWF0IjoxNTI5Njc4NzgxfQ.eyJpZCI6MX0.EyoFH3Y6LMVdj6hVNRhvJvQa3cPrZq0b4M6fXVZJ7qo"
headers = {'accesstoken':token}
# r = requests.post("http://127.0.0.1:5000/login", data=user_info, headers=headers)
r = requests.post("http://127.0.0.1:5000/user/110/orders", data=data, headers=headers)
# r = requests.get("http://127.0.0.1:5000/user/110/orders", headers=headers)
# r = requests.post("http://127.0.0.1:5000/sign_up", data=user_info)
# r = requests.get("http://127.0.0.1:5000/api/token",auth=(user_info['username'],user_info['password']))
# r = requests.get("http://127.0.0.1:5000/api/resource",auth=(token, '222'))

# s = requests.get("http://127.0.0.1:5000/search", params=params)

print (r.text)
# print (r.cookies['phone_num'], r.cookies['password'])
# print (l.text)

# real_ip = request.headers.get('X-Real-Ip', request.remote_addr)
 # ip = request.remote_addr
 # request.headers['Authorization']
