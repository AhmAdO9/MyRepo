import requests
from bs4 import BeautifulSoup
import json
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=macbook+pro&_sacat=0"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all("div",class_="s-item__info clearfix")
for item in items:
    print(item."span", class_='s-item__price')




# price = soup.find_all("span", class_="s-item__price")
