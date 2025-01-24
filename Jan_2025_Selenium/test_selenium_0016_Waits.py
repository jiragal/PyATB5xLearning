import pytest
import allure
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Testing wait functionality")
@allure.description("Verify the error message, if user entered wrong password")
@pytest.mark.negativetesting
def test_negative_app_vwo_com():
    path = 'https://app.vwo.com/#/login'
    driver = webdriver.Chrome()
    driver.get(path)

    # Now we need to implicitly wait for page to load
    driver.implicitly_wait(5)

    email_web_element = driver.find_element(By.ID, "login-username").send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.NAME, "password").send_keys("password@1234")

