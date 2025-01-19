# Explicit Wait: In Selenium it is used to tell the Web Driver to wait for certain conditions
# (Expected Conditions) or maximum time exceeded before throwing “ElementNotVisibleException” exception.
import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# WebDriverWait is a class in Selenium that allows you to
# wait for specific conditions to be met before continuing with a test.
# It's used to handle synchronization issues and ensure reliable test execution
from selenium.webdriver.support.wait import WebDriverWait

#An example is automating the task to check if all elements present on a web page, matching a particular locator, are visible.
from selenium.webdriver.support import expected_conditions as EC

@allure.title("App.vwo.com Explicit Wait")
@allure.description("Test to verify that 'app.vwo.com' is loaded with waits")
@pytest.mark.negativetestcase
def test_negative_testcase():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)
    user_id= driver.find_element(By.XPATH,"//*[@id='login-username']")
    pwd= driver.find_element(By.XPATH,"//input[@id='login-password']")
    user_id.send_keys("abc@gmail.com")
    pwd.send_keys("password@1234")
    submit_button= driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    submit_button.click()
    # Wait for the error message
    # A Condition to check the element
    # error_msg_element - comes after 2-4 seconds, there we need system has to wait
    # Add a condition so that Webdriver should wait for that condition.
    # Verify that message is visible.
    #time.sleep(5) # Python Int to wait for 5 seconds without any condition
    WebDriverWait(driver, timeout=5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"








