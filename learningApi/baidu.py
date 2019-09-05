import requests, re
from bs4 import BeautifulSoup as BS

s = requests.Session()
url = "https://passport.baidu.com/v2/api/?login"
headers= {
"Host": "passport.baidu.com",
"Referer": "https://www.baidu.com/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
account = 'tianenliu@126.com'  #账号
password = 'yongyi'  #密码
deploy =  {"username":account,"passwd":password}

r = s.post(url,json=deploy,headers=headers)
print(r.cookies)
print(r.status_code)
# print(r.text)
# print(r.cookies)

re = s.get("https://www.baidu.com/",headers=headers,allow_redirects = False)
print(re.cookies)
# print(re.text)
# print(re.cookies)
# print(r.encoding)

print("城市： " + BS(re.text, 'lxml').find("em", {"class": "show-city-name"})["data-key"])
print("气温： " + BS(re.text, 'lxml').find("em", {"class": "show-icon-temp"}).string)