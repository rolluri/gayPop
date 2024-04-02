from bs4 import BeautifulSoup
import bs4

import requests

import re

stAccept = 'text/html'

stUserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'

headers = {
    'Accept': stAccept,
    'User-Agent': stUserAgent
}

linkGet = 'https://genius.com/Iasdasdqwe'
if linkGet == '':
    link = 'https://genius.com/Instasamka-and-whate-lyrics'
else:
    link = linkGet

try:
    req = requests.get(link,headers) 
except BaseException:
    print(f'некорректная ссылка {link}')


src = req.text

soup = BeautifulSoup(src,'lxml')
title = soup.title.string
print(f'Название: {title}')
takeAllText = soup.find('div',class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL').get_text(separator=' ')
reText = re.sub(r'\[.{1,30}\]','',str(takeAllText))
print(f'Текст: {reText}')


textFile = open('textFile.txt','w+')
textFile.write(f'Название: {title}\nТекст: {reText}')
textFile.close()