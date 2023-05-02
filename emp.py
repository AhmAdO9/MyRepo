import requests

def get_articles(query):
    reports={
    "q" : query,
    "country" : "in",
    "api_key" : "ccd5c3a96e1c4c6a8fa3ee2f887a3e83"

    }
    response = requests.get("https://newsapi.org/v2/top-headlines?", query)
    articles1 = response.json()['articles']
    results = []

    for article in articles1:
        results.append({"title": article["title"]})
    
    for result in results:
        print(result["title"])


get_articles('football')
