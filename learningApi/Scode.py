import requests

r = requests.get('http://httpbin.org/get')
#状态码查询比对
print(r.status_code == requests.codes.ok)
#打印状态码
print(r.status_code)
#正常则显示为空
print(r.raise_for_status())
#打印响应头
print(r.headers)
#HTTP头部大小写不敏感，可用任意形式
#例子1
print(r.headers['Content-Type'])
#例子2
print(r.headers.get('content-type'))

# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# #抛出异常
# bad_r.raise_for_status()
