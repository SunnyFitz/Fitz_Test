# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import requests
from splinter.browser import Browser
import easygui as g

url = "https://kyfw.12306.cn/otn/leftTicket/init"
b = Browser(driver_name="chrome")
b.visit(url)

b.cookies.add({"_jc_save_fromStation":"%u82CF%u5DDE%2CSZH"})
b.cookies.add({"_jc_save_fromDate":"2018-02-12"})
b.cookies.add({u'_jc_save_toStation':'%u829C%u6E56%2CWHH'})

b.reload()
b.find_by_text(u"查询").click()

time.sleep(3)

b.find_by_text(u"登录").click()
b.fill("loginUserDTO.user_name","18362885680")
b.fill("userDTO.password","x15963")
time.sleep(1)
msg = "请点击验证码并登陆，完成后选择Continue,取消请点击Cancel"
title = "请选择"
az = 0
while 1:
    if g.ccbox(msg,title):
        az = 1
        break
    else:
        break
 
