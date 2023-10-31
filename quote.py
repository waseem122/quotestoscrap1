#This is quotes to scrap website scraping file
#x
import requests
from bs4 import BeautifulSoup

res = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.title.text)
print(res)