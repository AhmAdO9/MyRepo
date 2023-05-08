import csv
from bs4 import BeautifulSoup
import requests
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
new = soup.find_all("h3", class_="s-post-summary--content-title")


with open("stack_over_flow1.csv", "w") as file:
  element = csv.writer(file)
  for news in new:
            news1 = news.text          
            element.writerow([news1])