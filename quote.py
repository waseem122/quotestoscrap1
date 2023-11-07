#Scraping static website
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
res = requests.get(url)
print(res.text)