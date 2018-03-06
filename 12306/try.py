# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import requests


suc = 0
fai = 0
nu = 0

def refresh(count):
    global suc
    global fai
    global nu
    print (count)
    try:
        print("\n\n########## TEST SCRIPT ATTEMPT: {} ##########".format(nu))
        time.sleep(1)
        nu += 1
        suc += 1
 
        if (suc > count):
            return 1

        print('成功次数：',suc)
        refresh(count)

    except:
        print('失败次数：',fai)
        fai += 1

        if (fai > count):
            return 1
        refresh(count)



if __name__ == "__main__":
    count = input('请输入刷票次数：')
    count = int(count)
    refresh(count)
    
