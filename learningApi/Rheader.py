import requests

#带Header的
# headers = {"Content-Type": "application/json",
#             "token": "3d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4"}
# r = requests.post("http://127.0.0.1:5000/header",headers= headers)
# result = r.json()
# print(result)

#带Basic Auth认证的
auth = ("admin","admin123")
r = requests.post("http://127.0.0.1:5000/auth", auth = auth)
result = r.json()
print(result)
