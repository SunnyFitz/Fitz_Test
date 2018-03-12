# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

def check(key):
    response = requests.get('http://www.baidu.com/s?wd=' + key)
    print(response.text)
    print(response.json())
    #result = response.json()
    #return result['data']['result']

if __name__ == "__main__":
    key = input('请输入问题： ')
    check(key)
