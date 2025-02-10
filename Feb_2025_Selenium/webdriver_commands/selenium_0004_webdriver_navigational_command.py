import time
from selenium import webdriver
from selenium.webdriver.common.by import By

path1 = "http://www.amazon.com"

path2 = 'http://www.snapdeal.com'

driver = webdriver.Chrome()
driver.get(path1)
driver.maximize_window()
driver.get(path2)
driver.maximize_window()

# web_driver navigational commands now we will use
driver.back()
driver.forward()
driver.refresh()

time.sleep(5)
driver.quit()
