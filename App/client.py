import requests

user_info = {'phone': '110', 'password': '123'}
# cookies = {'phone_num': 'letian', 'password': '123'}
r = requests.post("http://127.0.0.1:5000/sign_up", data=user_info)
# l = requests.post("http://127.0.0.1:5000/login", cookies=cookies)

print (r.text)
# print (r.cookies['phone_num'], r.cookies['password'])
# print (l.text)