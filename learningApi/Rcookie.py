import requests
import requests.cookies

# url = 'http://httpbin.org/cookies'
# #cookies 赋值
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)
#
# #打印cookies
# url = 'https://www.matchvs.com'
# r = requests.get(url)
# print(r.cookies['cn.matchvs.com'])


jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain = 'heepbin.org', path='/cookies')
jar.set('gross_cookie','blech', domain = 'httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)


# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)
