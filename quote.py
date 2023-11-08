#Scraping static website
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
res = requests.get(url)
if res.status_code ==200:
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.prettify())

else:
    print('page is not found!')