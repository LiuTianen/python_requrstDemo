import requests
# 获取活动id
r = requests.get("http://127.0.0.1:5000/get_activity")
result = r.json()
print(result)
activity_id = result["data"]["id"]

#获取用户id
r = requests.get("http://127.0.0.1:5000/get_user")
result = r.json()
print(result)
user_id = result["data"]["id"]
#
# 调用获取抽奖号码接口
data = {"aid": activity_id, "uid": user_id}
r = requests.post("http://127.0.0.1:5000/lucky_number", data=data)
result = r.json()
print(result)