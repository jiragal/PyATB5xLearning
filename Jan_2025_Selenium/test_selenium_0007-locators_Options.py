import pytest
import allure
import time
from selenium import webdriver
#from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import service


# Headless is an execution mode for Firefox and Chromium based browsers.
# It allows users to run automated scripts in headless mode,
#                                     meaning that the browser window wouldn’t be visible.


@allure.title("Testing By.ID & By.NAME")
@allure.description("Verify the current url")
@pytest.mark.positivetest
class TestClass(object):
    def test_katalon_chrome(self):
        path = "https://katalon-demo-cura.herokuapp.com/"
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("__start-maximized")
        # chrome_options.add_argument("--window-size=900,600")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(path)

        find_make_appointment = driver.find_element(By.ID, "btn-make-appointment")
        find_make_appointment.click()
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        time.sleep(5)
