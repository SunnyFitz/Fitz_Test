import requests
import os
import re
from urllib import parse

def get_url(thing,count):
    data = parse.quote(thing)
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+ data + '&cl=1&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word='+ data + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=0&fr=&pn=30&rn=' + count +'&gsm=3c&1520307698898='
    res = requests.get(url)
    a = res.content
    #print(a)
    pic_url = re.findall(r'"thumbURL":"(https:.*?.jpg)',str(a))

    return pic_url

def save_pic(a,pic_url):
    count = 0
    for i in pic_url:
        print(i)
        count += 1
        a1 = requests.get(i)
        file_name = a + str(count) + '.jpg'
        #print(file_name)
        with open(file_name,'wb') as f:
           f.write(a1.content)
    print('已经存储图片数量为: ' + str(count))
if __name__ == '__main__':
    a = input('你想要搜索什么图片：')
    b = input("你想要多少张图片：")
    pic_url = get_url(a,str(b))
    save_pic(a,pic_url)
