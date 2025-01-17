import time, os

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# from selenium.webdriver.chrome.options import Options



class TestClass(object):
    @allure.title("VWO negative test case")
    @allure.description("Test to verify if user put wrong user_id or password")
    @pytest.mark.negativetest
    def test_login_vwo(self):
        path = "https://app.vwo.com/"
        # chrome_options = Options()
        driver = webdriver.Chrome()
        driver.get(path)
        # Enter "Email address" @ Password
        driver.find_element(By.ID, "login-username").send_keys("admin")
        driver.find_element(By.ID, "login-password").send_keys("3u5t8Q3eb!!eCH9")
        # Click on "Sign In" Button
        sign_in_button = driver.find_element(By.ID, "js-login-btn")
        sign_in_button.click()
        time.sleep(3)
        # Now capture error message into variable
        error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
        print(error_message_web_element.text)
        assert error_message_web_element.text == "Your email, password, IP address or location did not match"
        time.sleep(5)
        driver.quit()  # Everything we are closing
