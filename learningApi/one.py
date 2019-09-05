import requests
#最简单的接口调用
# r = requests.get("http://127.0.0.1:5000/")
# result = r.json()
# print(result)

#RESTful风格的API
# name = "tom"
# r = requests.get("http://127.0.0.1:5000/user/" + name)
# result = r.json()
# print(result)

#根据ID返回不同的结果
# uid = "1"
# r = requests.get("http://127.0.0.1:5000/id/" + uid)
# result = r.json()
# print(result)

#GET请求，一般用作获取数据接口
# r = requests.get("http://127.0.0.1:5000/phone/1")
# result = r.json()
# print(result)

#PUT请求，一般用作更新数据接口
# data = {"name":"华为手机", "price":"3999"}
# r = requests.put("http://127.0.0.1:5000/phone/1",data=data)
# result = r.json()
# print(result)

#DELETE请求, 一般用作删除数据接口
r = requests.delete("http://127.0.0.1:5000/phone/1")
result = r.json()
print(result)