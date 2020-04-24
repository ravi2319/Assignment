import requests
from bs4 import BeautifulSoup

URL = "https://www.indiatoday.in/india"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

