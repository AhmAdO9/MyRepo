from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class Manga():
       
        def anime(self):
            time.sleep(5)    
            browser = webdriver.Chrome()
            browser.maximize_window()
            browser.get("http://google.com")
            browser.find_element(By.CLASS_NAME, "gLFyf").send_keys("one piece manga online")
            browser.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']").click()
            browser.find_element(By.XPATH, "//a[@href='https://www.viz.com/shonenjump/chapters/one-piece']//h3[@class='LC20lb MBeuO DKV0Md']").click()
            time.sleep(3)
            # elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='javascript:void(0)']//i[@class='icon-close']")))
            browser.find_element(By.XPATH, "//div[@id='modal-follow']")
            browser.find_element(By.XPATH, "//a[@href='#modal-follow']//i[@class='icon-close']").click()
            # action.move_to_element(elem).click().perform()
            browser.find_element(By.XPATH, "//td[text()='March 26, 2023']").click()
            time.sleep(2)
            content = browser.find_element(By.XPATH, "//div[@class='noUi-touch-area']")
            action = ActionChains(browser)
            action.move_to_element(content).perform()
            time.sleep(2)
            action = ActionChains(browser)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)
            action.drag_and_drop_by_offset(content,-100,0).perform()
            time.sleep(2)


run = Manga()           
run.anime()
