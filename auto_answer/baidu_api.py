# -*- coding: UTF-8 -*-

from aip import AipOcr
import requests

APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath = "crop3.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

result = aipOcr.basicGeneral(get_file_content(filePath), options)
answers = [x['words'] for x in result['words_result'][-4:]]
question = ''.join(x['words'] for x in result['words_result'][:-4])
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
print (answers)
