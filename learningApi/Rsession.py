import requests

s = requests.Session()
r = s.post("http://127.0.0.1:5000/user_login",data={"username":"jack", "password":"123"})

print(r.cookies)

r2 = s.get("http://127.0.0.1:5000/user_data")

print(r2.cookies)