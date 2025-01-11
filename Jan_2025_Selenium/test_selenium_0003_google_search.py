import pytest
import allure
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://www.google.com/
# 3) Search for "google search through python"

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
full_url = "https://www.google.com/"
driver.get(full_url)
search = driver.find_element(By.NAME,"q")
search.send_keys("google search through python")
driver.find_element(By.NAME,"btnK").click()
driver.implicitly_wait(30)