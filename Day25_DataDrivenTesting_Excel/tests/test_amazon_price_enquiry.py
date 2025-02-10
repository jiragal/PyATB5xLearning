import allure, time, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select
from Day25_DataDrivenTesting_Excel.utils import utilsExcel

#Open a website amazon.com
#Input XL file is data.xlsx and it contains product details
#Extract the price of the first result
#Write the price back to excel file in Column Bsa

def test_price_enquiry():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/ref=nav_logo")
    driver.maximize_window()
    # define XL file location
    file = r'C:\Users\Sanjiva\Desktop\data.xlsx'
    rows = utilsExcel.getRowCount(file,"Sheet1")
    print(rows)
    # reading data from excel
    for r in range(2, rows+1):
        product_name = utilsExcel.readData(file,"Sheet1",r,1)
        #search_box
        search_box = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

        #wait for the page to load
        time.sleep(3)
        price = driver.find_element(By.CSS_SELECTOR,".a-price-whole").text
        print(f"Product: {product_name}, Price: {price}")
        #write the price to excel sheet
        utilsExcel.writeData(file,"Sheet1",r,2,data=price)

    driver.close()

