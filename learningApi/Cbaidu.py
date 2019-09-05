#-*- coding:utf-8 -*-
import time
import requests
from selenium import webdriver
"""
有错，后续处理
思路没错，需要后续调整
"""
def get_system_cookies(url,account,password):
    '''通过request 登陆系统，获取cookie'''
    cookiesList = []
    data = {"username":account,"passwd":password}
    roomSession  = requests.Session()
    roomSession.post(url,json=data)
    loadCookies = requests.utils.dict_from_cookiejar(roomSession.cookies)
    for cookieName,cookieValue in loadCookies.items():
        cookies = {}
        cookies['name'] = cookieName
        cookies['value'] = cookieValue
        cookiesList.append(cookies)
    return cookiesList

def is_login_status_succeed(driver):
    '''判断是否登陆状态，非登陆状态,通过cookie登陆'''
    loginUrl = 'https://passport.baidu.com/v2/api/?login'  #登陆地址
    account = 'tianenliu@126.com'  #账号
    password = 'yongyi'  #密码
    driver.get('https://www.baidu.com/') #测试是否为登陆状态
    loginTest = driver.find_element_by_css_selector("#u1 > a.lb").text
    if '登录' in loginTest:
        for cookie in get_system_cookies(loginUrl,account,password): 
            driver.add_cookie(cookie)  #添加cookie ，通过Cookie登陆
            print(cookie)
    # return driver

def request_circle_details(driver,requestUrl):
    ''''''
    is_login_status_succeed(driver)
    driver.get(requestUrl)
    verifyField = driver.find_element_by_css_selector('#s_icons > a.s-lite > span.title').text
    try:
        assert verifyField == '显示频道'
        return '测试通过'
    except AssertionError as e:
        return '测试未通过'

requestUrl = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.maximize_window()
print (request_circle_details(driver,requestUrl))
driver.get(requestUrl)
time.sleep(2)
driver.quit()