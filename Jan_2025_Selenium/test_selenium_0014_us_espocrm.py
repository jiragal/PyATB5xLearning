import allure
import pytest
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from November.ex_30112024_python_Class.Lab00060_Class_MethodOverriding_02 import Chrome


class TestClass(object):
    @allure.title("demo.us.espocrm.com positive espocrm case")
    @allure.description("Test to verify user is able to Login to the demo.us.espocrm.com")
    @pytest.mark.positive
    def test_login_espocrm(self):
        chrome_options = Options()
        load_dotenv()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("__start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(os.getenv("ESPOCRM"))
        click_button = driver.find_element(By.XPATH, "//button[@id='btn-login']")
        click_button.click()
        # Verify the current url
        expected_url = "https://demo.us.espocrm.com/?l=en_US"
        time.sleep(5)
        assert driver.current_url == expected_url
        driver.quit()

    @allure.title("demo.us.espocrm.com positive espocrm case")
    @allure.description("Test to verify user is able to click on Advanced Pack button")
    @pytest.mark.positive
    def test_advanced_pack(self):
        load_dotenv()
        driver = webdriver.Chrome()
        driver.get(os.getenv("ESPOCRM"))
        driver.maximize_window()
        element_pack = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/advanced-pack/']")
        element_pack.click()
        time.sleep(7)
        # expected_url = "https://www.espocrm.com/extensions/advanced-pack/"
        #
        # assert driver.current_url == expected_url
        driver.quit()

    @allure.title("demo.us.espocrm.com positive espocrm case")
    @allure.description("Test to verify user is able to click on 'Sales Pack' button")
    @pytest.mark.postive
    def test_sales_pack(self):
        load_dotenv()
        chrome_options= Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(os.getenv("ESPOCRM"))
        driver.maximize_window()
        element_sales_pack= driver.find_element(By.LINK_TEXT,"Sales Pack")
        element_sales_pack.click()
        time.sleep(7)
        driver.quit()

    @allure.title("demo.us.espocrm.com positive espocrm case")
    @allure.description("Test to verify user is able to click on 'Project Management' button")
    @pytest.mark.postive
    def test_project_management(self):
        load_dotenv()
        chrome_options= Options()
        chrome_options.add_argument("--incognito")
        driver=webdriver.Chrome(options=chrome_options)
        driver.get(os.getenv("ESPOCRM"))
        driver.maximize_window()
        element_button=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/extensions/project-management/']")
        element_button.click()
        time.sleep(7)
        driver.quit()

    @allure.title("demo.us.espocrm.com positive espocrm case")
    @allure.description("Test to verify user is able to click on 'Project Management' button")
    @pytest.mark.postive
    def test_personal_demo(self):
        load_dotenv()
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(os.getenv("ESPOCRM"))
        demo_element=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")
        demo_element.click()
        time.sleep(7)
        driver.quit()
