import pytest
import allure
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


@allure.title("vmo free-trial link click")
@allure.description("Test to verify the current page")
@pytest.mark.positive
class TestClass:
    def test_app_vwo_login_chrome(self):
        load_dotenv()
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(os.getenv("URL"))

        all_links_page = driver.find_elements(By.TAG_NAME, "a")
        print(len(all_links_page))
        for i in all_links_page:
            if "Start a free trial" in i.text:
                i.click()
            else:
                print("Not Found")

        time.sleep(5)
        driver.quit()  # Quit everything
