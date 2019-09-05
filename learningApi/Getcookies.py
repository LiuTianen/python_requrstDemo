from selenium import webdriver
from Page.LoginPage import Login_page
import time

driver = webdriver.Chrome()
driver.get("http://www.matchvs.com/login")

LoginPage = Login_page(driver)
LoginPage.open()
LoginPage.username("liutianen@outlook.com")
LoginPage.password("123qwe!@#")
LoginPage.loginbutton()
time.sleep(3)
# 获得cookie信息
cookie= driver.get_cookies()
"""方法尝试"""
# pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
# 将获得cookie的信息打印
print(cookie)


driver.quit()

"""
cookies 完整实现思路：
1、先使用request进行接口登录，get_cookies，直接requests.cookies保持
2、页面有验证码的情况下，先界面登录，获取cookies，然后add到请求里，进行登录
"""