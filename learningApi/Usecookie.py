from selenium import webdriver
driver = webdriver.Chrome()
import pickle
import requests
driver.get("http://www.matchvs.com/login")


# 添加Cookie
driver.add_cookie({'name':'matchvsAppKey','value':'ODI5UkRjbE1qSWxNeklsUURFeUpXVjNjVE15TVRJeUpVRXpKVEl5SldSeWIzZHpjMkZ3TWpJbFF6SWxNaklsYlc5akxtdHZiMngwZFc5QWJtVnVZV2wwZFdsc01qSWxRVE1sTWpJbFpXMWhibkpsYzNVeU1pVkNOeVU9N0U1'})
driver.add_cookie({'name':'cn.matchvs.com','value':'s%3AiigN_0MiuRwRyXhxQEajSgcbHKg8CgWx.EMfFevR23d6xPW7k1pFpPwVIm%2BmZnM32%2Fnp8sD%2BcOSE'})

# 刷新页面
driver.refresh()

"""方法尝试"""
# cookies = pickle.load(open("cookies.pkl",'rb'))
# s = requests.Session()
# for cookie in cookies:
#     s.cookies.set(cookie['name'],cookie['value'])
# response = s.get("https://www.matchvs.com/manage/gameContentList")
# 获取登录用户名并打印
username = driver.find_element_by_css_selector(".vsHeaderUserDataText").text
print(username)

#关闭浏览器
driver.quit()
