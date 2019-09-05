import requests

r = requests.get('https://www.baidu.com')

print(r.headers)
print(r.request.headers)