import requests
#屏蔽安全告警
import urllib3
urllib3.disable_warnings()
#Get 请求
payload = {'name':'python'}
headers = {'user-agent':'my-app/0.0.1'}

r = requests.get(url='https://www.v2ex.com/api/nodes/show.json',params=payload,headers=headers,verify = False)
#verify = False 不做SSL证书校验
#打印URL
print(r.url)
#打印响应编码
print(r.encoding)
#打印请求头部
print(r.headers)
#打印响应内容
print(r.text)
#打印二进制响应内容
print(r.content)
#打印json内容
"""要检查请求是否成功，使用 r.raise_for_status() 或者检查 r.status_code 是否和期望相同"""
print(r.status_code)
#打印请求Json
print(r.json())
#打印原始请求
print(r.raw)
#查看异常
print(r.raise_for_status())