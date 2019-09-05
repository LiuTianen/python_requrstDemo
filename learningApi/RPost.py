import requests
import json
#
#payload = {'key1': 'value1','key2':'value2'}

#元组列表,多个value使用一个key的时候
# payload = (('key','value1'),('key','value2'))
#
# r = requests.post("http://httpbin.org/post",data=payload)
# print(r.text)

#json格式的数据
# url = 'https://api.github.com/some/endpoint'
# payload = {'some':'data'}
# r = requests.post(url, data=json.dumps(payload))
# print(r.text)

#json直接传参
url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
r = requests.post(url, json=payload)
print(r.text)