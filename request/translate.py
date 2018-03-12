# -*- encoding = UTF-8 -*-

import urllib.request
import urllib.parse
import json

def youdao_translate(a):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}

    data['i'] = a
    data['doctype'] = 'json'
    data = bytes(urllib.parse.urlencode(data).encode("utf-8"))
    response = urllib.request.urlopen(url,data)
    html = response.read().decode("utf-8")
    target = json.loads(html)
    print('有道翻译结果是： ' + target['translateResult'][0][0]['tgt'])
    print(' ')

def google_translate(a):
    url = "https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&ssel=0&tsel=0&kc=2&tk=887997.779250&q=智障"
    data = {}

    data['q'] = a

    data = bytes(urllib.parse.urlencode(data).encode("utf-8"))
    print(data)
    response = urllib.request.urlopen(url)
    print(response)

    print('谷歌翻译结果是： ' + target['translateResult'][0][0]['tgt'])
    print(' ')

if __name__ == '__main__' :
    while 1:
        try:
            a = input("请输入要翻译的内容： ")
            youdao_translate(a)
            #google_translate(a)
        except:
            print('翻译出错~\(≧▽≦)/~啦啦啦')
