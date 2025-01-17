#In this program shows how to use LINK_TEXT and PARTIAL_LINK_TEXT
import pytest
import allure
import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


@allure.title("vmo freetrial link click")
@allure.description("Verify current url will hit if we click on free-trial button")
@pytest.mark.positivetestcase
class TestClass(object):
    def test_app_vwo_login_chrome(self):
        load_dotenv()
        chrome_options=Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(os.getenv("URL"))
        # LinkText and Partial Text
        # LINK_TEXT = It means EXACT Match
        # anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
        # anchor_tag_element.click()
        # time.sleep(2)

        # PARTIAL_LINK_TEXT - It means contains not exact value only partial text
        anchor_tag_elements = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
        anchor_tag_elements.click()
        time.sleep(2)

        expected_url = "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
        assert driver.current_url == expected_url
        driver.quit()   #Close everything

