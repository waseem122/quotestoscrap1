import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
res = requests.get(url)
if res.status_code == 200:
    #parse the webpage
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.title)

else:
    print('webpage is not there')