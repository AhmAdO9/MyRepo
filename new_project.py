import csv



from bs4 import BeautifulSoup
import requests
import json
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
new = soup.find_all("a", class_="s-link")
data = json.dumps(new)
print(data)






# with open("stack_over_flow.csv", "w") as file:
#         element = csv.writer(file)
#         for news in new:
#              news1 = news.text
#              element.writerow([news1])
             



   































# Your API key is: ccd5c3a96e1c4c6a8fa3ee2f887a3e83