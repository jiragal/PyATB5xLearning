# Web driver application related commands discussed

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Application related webdriver commands
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()
