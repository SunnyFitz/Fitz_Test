#！/usr/bin/env python
#-*- encoding = UTF-8 -*-

import os
import requests
from PIL import Image

def request(a):
    data = {
        'data': a,
        'output': 'image/gif',
        'error':'L',
        'type':'0',
        'margin':'0',
        'size':'4',
        
    }
    try:
        response = requests.get('http://tool.oschina.net/action/qrcode/generate', params=data)
        b = response.content 
        print('二维码获取成功')
        return b
    except:
        print('二维码获取出错')


def write_open(b):
    try:
        with open('erweima.png','wb') as f:
            f.write(b)
        im = Image.open('erweima.png')
        im.show()
        im.close()
        print('图片保存成功,路径为：' + os.getcwd() + '\\erweima.png')
    except:
        print('图片保存出错')

if __name__ == '__main__':
    a = input('请输入要转换的内容： ')
    b = request(a)
    write_open(b)
    
