import requests
from bs4 import BeautifulSoup
from Concert import Concert
from connect import db, concerts

countries = ['poland', 'czech-republic', 'netherlands']

for i in range(len(countries)):
    for j in range(1, 10):
        print(countries[i])
        print(j)
        URL = f'https://concertful.com/area/{countries[i]}/?page={j}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        concerts_arr = []
        for i in soup.findAll('div', {'class':'event_row'}):

            edate = i.find('div', {'class':'edate'})
            edate_meta = edate.find_all('meta')
            
            start_date = edate_meta[0]['content']
            end_date = edate_meta[1]['content']
            einfo = i.find('div', {'class':'einfo'})
            einfo_name = einfo.find_all('abbr')

            name = einfo_name[0].find_all('abbr')[0]['content']
            
            einfo_location = einfo.find_all('span')

            place = einfo_location[1].find_all('span')[1].string
            city = einfo_location[1].find_all('abbr')[1].string
            country = einfo_location[1].find_all('abbr')[2]['content']
            genre = einfo.find_all('span')[-1].string

            image = i.find_all('meta')[-1]['content']
            concert = Concert(name, start_date, end_date, city, country, place, genre, image)
            concerts_arr.append(concert.toObj())

        for concert in concerts_arr:
            concerts.update_one(
                {
                    'band':concert['band'],
                    'start date':concert['start date'],
                    'place':concert['place']
                },
                {
                    '$set': concert
                },
                True
            ) 
        