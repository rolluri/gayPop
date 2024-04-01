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
link = 'https://genius.com/Beyonce-and-dolly-parton-tyrant-lyrics'
req = requests.get(link,headers)

src = req.text

soup = BeautifulSoup(src,'lxml')
title = soup.title.string
print(f'Название: {title}')
takeAllText = soup.find('div',class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL').get_text(strip=True)
#reText = re.sub(r'\<.{1,69}\>','',str(tekeAllText))
print(takeAllText)
#textFile = open('textFile.txt','w+')
#textFile.write(takeAllText)
#textFile.close()
