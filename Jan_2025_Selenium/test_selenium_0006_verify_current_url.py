#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Verify the current URL

import pytest
import allure
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

@allure.title("Testing By.ID & By.NAME")
@allure.description("Verify the current url")
@pytest.mark.positivetest
class TestClass(object):
    def test_current_url(self):
        url = "https://katalon-demo-cura.herokuapp.com/"
        driver = webdriver.Chrome()
        driver.get(url)
        click_button = driver.find_element(By.ID,"btn-make-appointment")
        click_button.click()

        #Verify the current URL
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        time.sleep(5)
        driver.close() # close everything.

