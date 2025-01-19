import pytest,allure,time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver= webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    #To search whole body---> //table[contains(@id,'cust')]/tbody
    #We got XPATH for row = //table[contains(@id,'cust')]/tbody/tr
    #Now we will verify how many rows it has and column it has
    #Row--We will declare XPATH for row--
    row_elements=driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row_count=len(row_elements)
    print(row_count)

