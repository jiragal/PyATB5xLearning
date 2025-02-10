#In dynamic way of handling web tales
import time, allure,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_table():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    #Get a table
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table'] /tbody")
    #Get the row_table in two way
        #row_table_path= "//table[@summary='Sample Table']/tbody/tr[4]/td"
        #driver.find_element(By.XPATH,row_table_path)

    row_table= table.find_elements(By.TAG_NAME,"tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME,"td")
        print(" ")
        for e in cols:
            print(f"{e.text}")


