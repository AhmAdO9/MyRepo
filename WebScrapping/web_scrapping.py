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




   































# Your API key is: ccd5c3a96e1c4c6a8fa3ee2f887a3e83
>>>>>>> e5c5f4103a7575abe127fc5c216465f7cccf2143
