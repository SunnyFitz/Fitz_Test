# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import requests

def check():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-03-12&leftTicketDTO.from_station=SZH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT')
    #print(type(response.text))
    #print(type(response.json()))
    result = response.json()
    return result['data']['result']

suc = 0
fai = 0
nu = 1
resu = 3

# 31 一等座
# 30 二等座
# 26 无座

def refresh(count):
    global suc
    global fai
    global nu
    global resu
    try:
        print("\n\n########## TEST SCRIPT ATTEMPT: {} ##########".format(nu)) 
        time.sleep(1)
        nu += 1
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

        suc += 1
        print(resu)
        print('成功次数：{}'.format(suc))
        
        if (suc >= count):
            return 1
        refresh(count)
        
    except:
        fai += 1
        print('失败次数：',fai)

        refresh(count)

if __name__ == "__main__":
    count = input('请输入刷票次数：')
    count = int(count)
    refresh(count)
    
