import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://quotes.toscrape.com/page/{}/'

for i in range(1, 11):
    url = base_url.format(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    quotes = soup.find_all('span', class_ = 'text')
    author = soup.find_all('small', class_ = 'author')
   
    for x, y in zip(quotes, author):
        print(x.text)
        print(y.text)

#x