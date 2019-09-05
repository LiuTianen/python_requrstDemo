import requests

# r = requests.get('http://github.com')
# #
# print(r.url)
# #
# print(r.status_code)
# # 打印历史，显示是否有重定向发生
# print(r.history)
#
# #allow_redirects  控制重定向
# r = requests.get('http://github.com',allow_redirects = False)
# print(r.status_code)
#
# print(r.history)


# #HEAD, Requests 会自动处理所有重定向
# r = requests.head('http://github.com',allow_redirects = True)
# #
# print(r.url)
# #
# print(r.status_code)
# # 打印历史，显示是否有重定向发生
# print(r.history)


#timeout 控制连接请求过程的响应时间，与响应体的下载无关
requests.get('http://github.com',timeout =0.001)

