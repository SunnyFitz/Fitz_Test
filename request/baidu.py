 # -*- encoding = UTF-8 -*-

import requests
import json

def baidu_translate(a):
    url = "http://fanyi.baidu.com/v2transapi"
    data = {
        'from':'zh',
        'to':'en',
        'query':a,
        'transtype':'translang',
        'simple_means_flag':'3',
        'sign':'601208.905033',
        'token':'28ed5ff0fadd0871023623db700a42ea'
        }
    res = requests.post(url,data=data)
    print(res.content)
    


if __name__ == '__main__':
    a = input("请输入要翻译的内容： ")
    baidu_translate(a)
