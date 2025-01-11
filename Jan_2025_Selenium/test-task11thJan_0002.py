#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://demo.us.espocrm.com/
# 3) verify the title and current url
# 4) assert and create Allure HTML report also.

#Selenium4
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@allure.title("Demo testing")
@allure.description("Verify title and current URL")
def test_espocrm_demo():
    path = "https://demo.us.espocrm.com/"
    server_path = "C:/Users/Sanjiva/PycharmProjects/PyATB5xLearning/Jan_2025_Selenium/chromedriver.exe"
    serv_obj=Service(server_path)
    driver=webdriver.Chrome(service=serv_obj)
    driver.get(path)
    actual_title = driver.title
    expected_title = "EspoCRM Demo"
    assert actual_title == expected_title
    current_url = driver.current_url
    assert current_url == path

