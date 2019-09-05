import requests


url = "https://testerhome.com/account/sign_in"
userUrl = "https://testerhome.com/setting"
payload = {
    # "utf8":"✓",
	"user[login]":"869045001@qq.com",
	"user[password]":"yongyi088",
	"user[remember_me]":0,
	"commit":"登录"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "testerhome.com",
    }
headerss = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
s = requests.Session()

r1 = s.post(url, data=payload, headers=headers)
# print(response.text)
print(r1.cookies)
print(r1.url)
# print(r1.headers)


r = s.get(userUrl,headers=headerss)
print(r.url)
print(r.cookies)
# print(r.status_code)
# print(r.text)