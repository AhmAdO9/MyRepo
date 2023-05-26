from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome()
browser.get("https://stackoverflow.com/questions")
x = browser.find_elements(By.XPATH, ("""//h3[@class='s-post-summary--content-title']//a"""))
for i in x:
    print(i.get_attribute("text"))

# response = requests.get(x)
# soup= BeautifulSoup(response.text, "html.parser")
# data = soup.select('yt-formatted-string[id="content-text" ]')
# print(data)
