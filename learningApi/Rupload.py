import requests

files = {'file': open('D:\\log.txt', 'rb')}
r = requests.post("http://127.0.0.1:5000/upload",files = files)
result = r.json()
print(result)
