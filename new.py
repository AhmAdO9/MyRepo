import requests
from bs4 import BeautifulSoup

api_key = "ccd5c3a96e1c4c6a8fa3ee2f887a3e83"
url = "https://newsapi.org/docs/endpoints/top-headlines"
params = {


            api_key : "ccd5c3a96e1c4c6a8fa3ee2f887a3e83",
            "country" : "in"

}


response = requests.get(url, params)

print(response.text)