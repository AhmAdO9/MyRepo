from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.get("http://google.com")
browser.find_element(By.CLASS_NAME, "gLFyf").send_keys("fit girl repacks")
time.sleep(1)
browser.find_element(By.XPATH, "//div[@class='wM6W7d']/span/b[text()='fitgirl']").click()
browser.find_element(By.XPATH, "//h3[text()='FitGirl Repacks - Page 9 of 351']").click()
action = ActionChains(browser)
elem = browser.find_element(By.XPATH, "//h1/a[@href='https://fitgirl-repacks.site/way-of-the-hunter/']")
action.move_to_element(elem).click().perform()
browser.find_element(By.XPATH, "//ul/li/a[3][@href='https://pastefg.hermietkreeft.site/?19095bfd2aa4d816#2NGRs3TB3bLq2KcPi1SBtaxLCff2JZhKDzRZsLtxv9Kf']").click()
browser.find_element(By.XPATH, "//a[@href='magnet:?xt=urn:btih:CA2858D0EB735535F20ACC56EE40DE52351A496A&dn=Way+of+the+Hunter+%28v1.22.0.93361+%2B+3+DLCs+%2B+Windows+7+Fix%2C+MULTi16%29+%5BFitGirl+Repack%5D&tr=udp%3A%2F%2Fopentor.net%3A6969&tr=udp%3A%2F%2Fopentor.org%3A2710&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta-net.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce']").click()





