import pyautogui as py
import time

# print(py.position())

time.sleep(5)
py.moveTo(673,1058,0.5)
py.click()


py.moveTo(910,570,0.8)
py.click()

py.moveTo(1000,342,0.8)
py.click()

py.moveTo(1254,245,0.8)
time.sleep(1)

py.dragTo(1150,245,3, button="left")
py.click()

py.moveTo(1349,85,0.8)
py.click()

py.moveTo(673,1058,0.5)
py.click()


py.moveTo(1200,985,0.5)
py.click()


py.moveTo(1210,875,0.5)
py.doubleClick()
