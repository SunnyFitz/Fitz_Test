# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import requests
import random
import easygui as g
from splinter.browser import Browser

suc = 0
fai = 0
nu = 3
count = 1

def check():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-03-06&leftTicketDTO.from_station=SZH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT')
    #print(type(response.text))
    #print(type(response.json()))
    result = response.json()
    return result['data']['result']

def find():
    
    resu = 3
    
    for i in check():
        tmp_list = i.split('|')

        if tmp_list[31] != '无' and tmp_list[31] != '':     
            print('一等座有票',tmp_list[3],'发车时间',tmp_list[8])
        if tmp_list[30] != '无' and tmp_list[30] != '':
            print('二等座有票',tmp_list[3],'发车时间',tmp_list[8])
        if tmp_list[26] != '无' and tmp_list[26] != '':
            print('无座有票',tmp_list[3],'发车时间',tmp_list[8])

        if tmp_list[3] == 'G7084':
            if tmp_list[30] != '无' and tmp_list[30] != '':
                resu = 1
                #open().b.find_by_text(u"预订")[6].click()

        elif tmp_list[3] == 'G7132':
            if tmp_list[30] != '无' and tmp_list[30] != '':
                resu = 2
                #open().b.find_by_text(u"预订")[7].click()        
            #open().b.find_by_text(u"查询").click()

    return resu


if __name__ == "__main__":


    url = "https://kyfw.12306.cn/otn/leftTicket/init"
    b = Browser(driver_name="chrome")
    b.visit(url)

    b.cookies.add({"_jc_save_fromStation":"%u82CF%u5DDE%2CSZH"})
    b.cookies.add({"_jc_save_fromDate":"2018-03-06"})
    b.cookies.add({u'_jc_save_toStation':'%u829C%u6E56%2CWHH'})

    b.reload()
    b.find_by_text(u"查询").click()

    time.sleep(3)

    b.find_by_text(u"登录").click()
    b.fill("loginUserDTO.user_name","18362885680")
    b.fill("userDTO.password","x15963")
    msg = "请点击验证码并登陆，完成后选择Continue,取消请点击Cancel"
    title = "请选择"
    az = 0
    while 1:
        if g.ccbox(msg,title):
            az = 1
            break
        else:
            break

    b.find_by_text(u"车票预订").click()
    time.sleep(1)
    b.find_by_text(u"查询").click()
    while 1:

        try:
            print("\n\n##########  SCRIPT ATTEMPT: {} ##########".format(count)) 
            count += 1
            time.sleep(1)
            
            resu = find()
            resu = str(resu)
            print (resu)




            if resu =='1':
                print('G7084有票')
                b.find_by_text(u"车票预订").click()
                time.sleep(1)
                b.find_by_text(u"查询").click()
                time.sleep(1)
                b.find_by_text(u"预订")[4].click()
                time.sleep(1)
                b.find_by_text(u"高仁豪").click()
                time.sleep(1)
                b.find_by_text(u"提交订单").click()
                time.sleep(1)
                b.find_by_text(u"确认").click()
                break
            elif resu =='2':
                print('G7132有票')
                b.find_by_text(u"车票预订").click()
                time.sleep(1)
                b.find_by_text(u"查询").click()
                time.sleep(1)
                b.find_by_text(u"预订")[5].click()
                time.sleep(1)
                b.find_by_text(u"高仁豪")[1].click()
                time.sleep(1)
                b.find_by_text(u"提交订单").click()
                time.sleep(1)
                b.find_by_text(u"确认").click()
                break
            elif resu =='3':
                print('无票')

            aw = random.random() + 1       
            time.sleep(aw)
                

        except:
            print ('查询超时')
            pass

    print('抢票成功')


        


