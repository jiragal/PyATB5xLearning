from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pytest, allure

class TestClass():
    #######   find_elements() - Returns single webElements
    @allure.title("Locator matching with single webelement")
    @allure.description("Test to verify locator is matching with single web_element")
    @pytest.mark.positivetestcase
    def test_single_webelement(self):
        driver =webdriver.Chrome()
        driver.get("https://demo.nopcommerce.com/")
        element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
        element.send_keys("phone")


    @allure.title("Locator matching with multiple webelements")
    @allure.description("Test to verify locator is matching with multiple elements")
    @pytest.mark.positivetestcase
    def test_multiple_webelement(self):
        driver=webdriver.Chrome()
        driver.get("https://demo.nopcommerce.com/")
        elements=driver.find_element(By.XPATH,"//div[@class='footer']//a")
        print(elements.text)

    @allure.title("Element not available then throw NoSuchElementException")
    @allure.description("Test to verify if element not available "
                        "then system throw NoSuchElementException ")
    @pytest.mark.negativetestcase
    def test_noSuchElementException(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.nopcommerce.com/")
        elements = driver.find_element(By.LINK_TEXT,"Log")
        elements.click()

    #######   find_elements() - Returns multiple webElements

    @allure.title("Locator matching with multiple webelements")
    @allure.description("To verify driver finds multiple webelemts")
    @pytest.mark.positivetestcase
    def test_find_elements_multiple(self):
        driver=webdriver.Chrome()
        driver.get("https://demo.nopcommerce.com/")
        elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
        print(len(elements))   #23
        print(elements[0].text)   #Sitemap
        for item in elements:
            print(item.text)




