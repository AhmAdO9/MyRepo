from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Manga():
       
        def anime(self):
            time.sleep(5)    
            browser = webdriver.Chrome()
            browser.implicitly_wait(3)
            browser.maximize_window()
            browser.get("http://google.com")
            browser.find_element(By.CLASS_NAME, "gLFyf").send_keys("one piece manga online")
            browser.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']").click()
            browser.find_element(By.XPATH, "//a[@href='https://www.viz.com/shonenjump/chapters/one-piece']//h3[@class='LC20lb MBeuO DKV0Md']").click()
            browser.find_element(By.XPATH, "//div[@id='modal-follow']")
            browser.find_element(By.XPATH, "//a[@href='#modal-follow']//i[@class='icon-close']").click()
            browser.find_element(By.XPATH, "//td[text()='March 26, 2023']").click()
            content = browser.find_element(By.XPATH, "//div[@class='noUi-touch-area']")
            action = ActionChains(browser)
            action.move_to_element(content).perform()
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
