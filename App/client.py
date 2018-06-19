import requests

data = "{'username': '111', 'password': '222'}"
user_info = {'username': '111', 'password': '222'}
# user_info = {'phone': '110', 'password': '123'}
# params = {'type': 'dessert'}
token ="eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyOTQwNTc0MSwiaWF0IjoxNTI5NDA1MTQxfQ.eyJpZCI6MX0.WzZyCbI_g7rtpCRWmB360eYTxbk-Rk7kQswYhZsjm3k"
headers = {'accesstoken':token}
# r = requests.post("http://127.0.0.1:5000/login", data=user_info, headers=headers)
r = requests.post("http://127.0.0.1:5000/user/110/orders", data=data, headers=headers)
# r = requests.get("http://127.0.0.1:5000/user/110/orders/1", headers=headers)
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
