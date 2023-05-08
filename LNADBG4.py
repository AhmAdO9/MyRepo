import csv
from bs4 import BeautifulSoup
import requests
response = requests.get("https://lnadbg4.adb.org/oga0009p.nsf/sancALL1P?OpenView&count=999")
soup = BeautifulSoup(response.text, "html.parser")
new = soup.find_all("table", border="0")
# for news in new:
#     print(f"{news.text}")

with open("Table.csv", "w", encoding="utf-8") as file:
  element = csv.writer(file)
  for news in new:
            news1 = news.text          
            element.writerow([news1])