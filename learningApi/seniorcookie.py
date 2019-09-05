import requests


#跨请求保持cookie
# s = requests.Session()
#
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
#
# print(r.text)

#方法级别的参数不会被跨请求保持
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies = {'from-my':'browser'})
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)

