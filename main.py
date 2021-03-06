import requests
import re
from bs4 import BeautifulSoup

URL = 'https://concertful.com/area/poland/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
infos = []
bands = []

for i in soup.findAll('div', {'class':'einfo'}):
    infos.append(i)
    bands.append(i.span.a.string)
