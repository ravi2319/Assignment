import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.indiatoday.in/india"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

headlines = []

table = soup.find('main', attrs = {'id' : 'main'})

for row in table.findAll('div', attrs = {'class' : 'catagory-listing'}):
    headline = {}
    headline['theme'] = row.h2.text
    headline['url'] = row.a['href']
    headline['img'] = row.img['src']
    headlines.append(headline)

filename = 'try.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img'])
    w.writeheader()
    for headline in headlines:
        w.writerow(headline)
