# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import requests
from splinter.browser import Browser
import easygui as g

msg = "请点击验证码并登陆，完成后选择Continue,取消请点击Cancel"
title = "请选择"
az = 0
while 1:
    if g.ccbox(msg,title):
        az = 1
        break
    else:
        break
