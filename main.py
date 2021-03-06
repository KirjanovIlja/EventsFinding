import requests
import re
from bs4 import BeautifulSoup
from Concert import Concert

URL = 'https://concertful.com/area/poland/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
infos = []
bands = []
abbrs = []

for i in soup.findAll('div', {'class':'einfo'}):
    infos.append(i)
    bands.append(i.span.a.string)
    #band = i.abbr.find_all('abbr')[0]['content']
    #link = i.abbr.find_all('abbr')[1]['content']
    
    print(i.find_all('<span class="elocation">'))
    #print(band, link)

print(infos[0].prettify())
