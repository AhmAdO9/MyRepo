import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import sys
import re

options= Options()
browser = uc.Chrome(options=options)
browser.maximize_window()
browser.get("""https://www.acnc.gov.au/""")
browser.implicitly_wait(10)
with open("1000 ABN (1).csv", "r") as abn:
    for i in abn:
        browser.find_element(By.XPATH, """//button[@class="btn btn-primary btn-large action-button btn-flat"]""").click()
        browser.find_element(By.XPATH, """//a[@href="/auth/login/hiring-drive-web-scraping-python-programmer-1684743290"]""").click() 
        browser.find_element(By.XPATH, """//input[@placeholder="Your username or email"]""").send_keys("thomasshel68@gmail.com")
        browser.find_element(By.XPATH, """//input[@placeholder="Your password"]""").send_keys("Fah@19318")
        browser.find_element(By.XPATH, """//button[@type="submit"]""").click()
        browser.find_element(By.XPATH, """//div[@class="span12"] //a[@href="/contests/hiring-drive-web-scraping-python-programmer-1684743290/challenges/match-names-1"]""").click()
        browser.find_element(By.XPATH, """//a[@href="https://www.hackerrank.com/external_redirect?to=https://www.acnc.gov.au/charity/charities"]""").click()
        handle = browser.window_handles
        browser.switch_to.window(handle[1])
        browser.find_element(By.XPATH, """//button[@id="go-to-external"]""").click()
        browser.find_element(By.XPATH, """//a[@data-cta-id="find-charity"]""").click()
        browser.find_element(By.XPATH, """//a[text()="Search the Charity Register"]""").click()
        time.sleep(10)    
    



























        # for i in x:
        #     print(i.get_attribute("text"))
 
    # response = requests.get(x)
# soup= BeautifulSoup(response.text, "html.parser")
# data = soup.select('yt-formatted-string[id="content-text" ]')
# print(data)
# //input[@type="email"]

# browser.find_element(By.XPATH, """//a[text()="Search the Charity Register"]""").click()

