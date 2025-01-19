#Fluent Wait: Fluent Wait instance defines the maximum amount of time
#to wait for a condition as well as the frequency with which to check the condition
#   -	Exception - NoSuchElementException
#   -	Waiting 30 seconds for an element to be present on the page,
#   -                                     checking for its presence once every 5 seconds

import allure,time,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("app.vwo.com")
@allure.description("To verify the error message should trigger if user entered wrong id or pwd")
def test_negative_case_vmo_login():
    driver= webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)



