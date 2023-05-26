from bs4 import BeautifulSoup
import requests


payload = {'api_key':'fad18a2d9c10564534e0108b6df31366',
           'url':'https://www.amazon.in/s?k=metal+detector&crid=2HD3JR6WL3X63&sprefix=metal+detector%2Caps%2C395&ref=nb_sb_noss_1'}
# HEADERS = ({})
response = requests.get("http://api.scraperapi.com", params=payload)
soup = BeautifulSoup(response.text, "html.parser")


Descrp = soup.select('a[class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
box = []
for b in Descrp:
    box.append(b.get('href'))

data = soup.select('a[class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

data1 = soup.select('span[class="a-size-base-plus a-color-base a-text-normal"]')
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


file = open('amazon17.csv', 'w',  encoding="utf-8")
for d in data:

    for elem in container:
            
            for p in prices:     
                             
                    for r in ratings:    
                                            
                            for rev in reviews:    
                                                                                                                                                          
                                    file.write(elem)
                                    file.write("\n")
                                    file.write(d.get("href"))
                                    file.write("\n")
                                    file.write(f"${p}")
                                    file.write("\n")
                                    file.write(f"Ratings:{r}")
                                    file.write("\n")
                                    file.write(f"Reviews:{rev}")
                                    file.write("\n")     

                                    for c in box:   
                                                
                                            payload = {'api_key':'fad18a2d9c10564534e0108b6df31366','url':f"https://www.amazon.in{c}"}
                                            response1 = requests.get("http://api.scraperapi.com", params=payload)
                                            soup1 = BeautifulSoup(response1.text, "html.parser")
                                            table = soup1.select('ul[class="a-unordered-list a-vertical a-spacing-mini"] li span')  
                                            for comment in table:
                                                file.write(comment.text)
                                            file.write("\n\n\n")
                                            container.pop(0)
                                            prices.pop(0) 
                                            ratings.pop(0)
                                            reviews.pop(0)
                                            box.pop(0)
                                            break



                                    break
                                    


                            break
                            

                    break
                    

            break
            
 
file.close()


