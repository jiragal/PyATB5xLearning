import pytest, allure, time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    # To search whole body---> //table[contains(@id,'cust')]/tbody
    # We got XPATH for row = //table[contains(@id,'cust')]/tbody/tr
    # Now we will verify how many rows it has and column it has
    # Row--We will declare XPATH for row--
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row_count = len(row_elements)
    print(row_count)

    # Find now number of columns
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col_count = len(col_elements)
    print(col_count)

    # print all the Rows and Column Value
    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row_count + 1):
        for j in range(1, col_count + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            # print(dynamic_path)
            data = driver.find_element(By.XPATH, dynamic_path)
            print(data.text, end=' ')

    # Find "Helen Bennett' belongs to which country

    for i in range(2, row_count + 1):
        for j in range(1, col_count+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"\n Helen Bennett is in {country_text}")
