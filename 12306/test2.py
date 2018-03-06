# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import random
import requests
import easygui as g
from splinter.browser import Browser

def check():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-12&leftTicketDTO.from_station=SZH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT')
    #print(type(response.text))
    #print(type(response.json()))
    result = response.json()
    return result['data']['result']

def find():
    nu = 0

    for i in check():
        tmp_list = i.split('|')
        #print(tmp_list)
    #for n in tmp_list:
    #    print(nu,n)
    #    nu += 1
    #nu = 0
        if tmp_list[3] == 'G7084':
            if tmp_list[30] != '无' and tmp_list[30] != '':
                nu = 1
                #open().b.find_by_text(u"预订")[6].click()

        elif tmp_list[3] == 'G7132':
            if tmp_list[30] != '无' and tmp_list[30] != '':
                nu = 2
                #open().b.find_by_text(u"预订")[7].click()        
        else:
            nu = 3
            #open().b.find_by_text(u"查询").click()

    return nu





while 1:
    xb = find()
    print (xb)
    time.sleep(3.2)


