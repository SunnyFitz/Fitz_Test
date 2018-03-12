 # -*- encoding = UTF-8 -*-

import requests
import random
import hashlib
import json
import urllib

def baidu_translate(a):

    httpClient = None
    myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    q = a
    fromLang = 'auto'
    toLang = 'en'
    appid = '20180211000122327'
    secretKey = 'XWD9nROtYDIA62AW8yfH'
    #salt = random.randint(32768, 65536)
    salt = 1435660288

    sign = appid + q + str(salt) + secretKey
    print(sign)
    m1 = hashlib.md5()
    m1.update(sign.encode('UTF-8'))
    key1 = m1.hexdigest()
    print(q)
    myurl = myurl+'?q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&appid='+appid+'&salt='+str(salt)+'&sign='+key1    
    b = requests.get(myurl)
    print(myurl)
    print(b)
    c = b.json()
    print(c)
    
    


if __name__ == '__main__':
    a = input("请输入要翻译的内容： ")
    baidu_translate(a)
