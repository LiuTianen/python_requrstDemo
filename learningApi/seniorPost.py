import requests

url = 'http://httpbin.org/post'

#上传文件
# files = {'file':open('report.xls','rb')}
#显示了文件名，文件类型，请求头
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

#接收字符串
files = {'file':('report.csv','some,data,to,send\nanother,row,to,send\n')}

r= requests.post(url, files=files)
print(r.text)

