from bs4 import BeautifulSoup
import requests

payload = {'api_key':'',
           'url':'https://www.amazon.in/s?k=soda+maker&sprefix=soda%2Caps%2C421&ref=nb_sb_ss_ts-doa-p_2_4'}
# HEADERS = ({})
response = requests.get("http://api.scraperapi.com", params=payload)
soup = BeautifulSoup(response.text, "html.parser")


data = soup.select('a[class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')


data1 = soup.select('span[class="a-size-medium a-color-base a-text-normal"]')
container=[]
for content in data1:
    container.append(content.text)

data2 = soup.select('span[class="a-price-whole"]') 
prices = []
for price in data2:
    prices.append(price.text)


data3 = soup.select('span[class="a-size-base s-underline-text"]')
ratings = []
for rate in data3:
    ratings.append(rate.text)


data4 = soup.select('span[class="a-icon-alt"]')
reviews = []
for review in data4:
    reviews.append(review.text) 



file = open('amazon6.csv', 'w',  encoding="utf-8")
for d in data:
    count = 0
    for elem in container:
        if count == 0:
            for p in prices:
                if count == 0:
                    for r in ratings:
                        if count == 0:
                            for rev in reviews:
                                if count == 0:        
                                    file.write(elem)
                                    file.write("\n")
                                    file.write(d.get("href"))
                                    file.write("\n")
                                    file.write(f"${p}")
                                    file.write("\n")
                                    file.write(f"Ratings:{r}")
                                    file.write("\n")
                                    file.write(f"Reviews:{rev}")
                                    file.write("\n\n\n")
                                    container.pop(0)
                                    prices.pop(0) 
                                    ratings.pop(0)
                                    reviews.pop(0)
                                    count +=1


                                else:
                                    pass


                        else:
                            pass

                else:
                    pass

            else:
                pass
 
file.close()


