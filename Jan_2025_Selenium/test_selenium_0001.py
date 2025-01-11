import pytest
import allure
import os
from selenium import webdriver

# # create a new Firefox session
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.maximize_window()
# # navigate to the application home page
# full_url = "https://business.adobe.com/"
# driver.get(full_url)

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
full_url = "https://business.adobe.com/"
driver.get(full_url)