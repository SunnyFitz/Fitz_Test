
import os
import time
import random
import requests
import subprocess
import pytesseract

from aip import AipOcr
from PIL import Image

config = {
    '1':(80,500,1000,880),
    'point':[
        (316,993,723,1078),
        (316,1174,723,1292),
        (316,1366,723,1469),
        (316,1570,723,1657),
        ]
    }


def get_screenshot():
    os.system('adb shell screencap -p /sdcard/test.png')
    os.system('adb pull /sdcard/test.png .')
    
def pic():
    img = Image.open('test.png')
    
    region = (100,370,970,570)
    cropImg1 = img.crop(region)
    cropImg1= cropImg1.convert('RGB')
    #cropImg1.save(r'C:\Users\wuzfigao\Desktop\New folder\crop.jpg')

    region = (100,600,970,1270)
    cropImg2 = img.crop(region)
    cropImg2= cropImg2.convert('RGB')
    #cropImg2.save(r'C:\Users\wuzfigao\Desktop\New folder\crop2.jpg')

    toImage = Image.new('RGBA',(870,870))
    region = (0,0,870,200)
    toImage.paste(cropImg1,region)
    region = (0,200,870,870)
    toImage.paste(cropImg2,region)
    toImage= toImage.convert('RGB')
    toImage.save(r'C:\Users\wuzfigao\Desktop\pythonn\New folder\crop3.jpg')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_question():
    APP_ID = '9851066'
    API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
    SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    filePath = "crop3.jpg"


    options = {
      'detect_direction': 'true',
      'language_type': 'CHN_ENG',
    }

    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    answers = [x['words'] for x in result['words_result'][-3:]]
    question = ''.join(x['words'] for x in result['words_result'][:-3])

    for i in range(len(answers)):
        answers[i] = answers[i][2:]
    print(question)
    print(answers)


    url = 'https://www.baidu.com/s'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    data = {
        'wd' : question
        }
    res = requests.get(url,params = data ,headers = headers)
    res.encoding = 'utf-8'
    html = res.text
    for i in range(len(answers)):
        answers[i] = (html.count(answers[i]),answers[i],i)

    answers.sort(reverse = True)
    print(answers)
    return answers

def click(point):
    cmd = 'adb shell input swipe %s %s %s %s %s' % (
        point[0],
        point[1],
        point[0] + random.randint(0,3),
        point[1] + random.randint(0,3),
        200
        )
    os.system(cmd)
    
def run():
    #get_screenshot()
    pic()
    res = get_question()
    #click(config['point'][res[0][2]])

if __name__ == "__main__":
    while 1:
        input('回车开始：')
        #time.sleep(.5)
        run()
