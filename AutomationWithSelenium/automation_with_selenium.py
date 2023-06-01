from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get("http://www.hackerrank.com/domains/python")
context = browser.find_element(By.XPATH, "//button[@data-analytics='NavBarLoginIcon']").click()
context3 = browser.find_element(By.ID, "input-1")
context3.send_keys("")
context4 = browser.find_element(By.ID, "input-2")
context4.send_keys("1")
context5 = browser.find_element(By.XPATH, "//span[text()='Log In']").click()
action = ActionChains(browser)
a = browser.find_element(By.XPATH, "//input[@value='solved']")
action.move_to_element(a).click().perform()
context7 = browser.find_element(By.XPATH, "//h4[text()='Say \"Hello, World!\" With Python']")


with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow([context7.text])
    

print("Done!")





#context4 = browser.find_element(By.XPATH, "//div[@jsname='V1ur5d']")
#context4.click()
