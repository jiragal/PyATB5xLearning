#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://demo.nopcommerce.com/
# 3) In this program demonstrate only how By.ID & By.NAME works
# 4) In search box search "Laptop"
# 4) assert and create Allure HTML report also.

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
import time,os

@allure.title("Testing new website search functionality")
@allure.description("Test to verify search box functionality")
@pytest.mark.systemtesting
class TestClass(object):
    def test_search_box(self):
        path = "https://demo.nopcommerce.com/"
        server_path = "C:/Users/Sanjiva/PycharmProjects/PyATB5xLearning/Jan_2025_Selenium/chromedriver.exe"
        service_obj = Service(server_path)
        driver = webdriver.Chrome(service=service_obj)
        driver.get(path)
        driver.maximize_window()  #maximize the window
        #time.sleep(500)
        driver.find_element(By.ID,"small-searchterms").send_keys("Asus N551JK-XO076H Laptop")
        driver.find_element(By.NAME,"q").send_keys("Asus N551JK-XO076H Laptop")
        time.sleep(10)