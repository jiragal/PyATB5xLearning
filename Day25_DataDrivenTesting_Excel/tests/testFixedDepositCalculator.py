import time,pytest,allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Day25_DataDrivenTesting_Excel.utils import utilsExcel



def test_FD_calculator():
    driver = webdriver.Chrome()
    driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
    # Set up the WebDriver
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[@id='wzrk-cancel']").click()
    driver.maximize_window()

    #define XL file location
    file = r'D:\DELL DATA\Documents\PavanKumar_Python\Day25-DataDrivenTesting_Excel\ClassExamples (2)\ClassExamples\caldata.xlsx'
    rows =utilsExcel.getRowCount(file,"Sheet2")
    print(rows)

    for r in range(2, rows+1):
        # reading data from excel
        pric = utilsExcel.readData(file,"Sheet2",r,1)
        rateofinterest = utilsExcel.readData(file,"Sheet2",r,2)
        per1 = utilsExcel.readData(file,"Sheet2",r,3)
        per2 = utilsExcel.readData(file,"Sheet2",r,4)
        free = utilsExcel.readData(file,"Sheet2",r,5)
        maturity_value_Rs = utilsExcel.readData(file,"Sheet2",r,6)

        # passing data to the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)
        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(free)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # Validation
        if float(maturity_value_Rs) == float(act_mvalue):
            print("test passed")
            utilsExcel.writeData(file,"Sheet2",r,8,"Passed")
            utilsExcel.fillGreenColor(file,"Sheet2",r,8)
        else:
            print("test failed")
            utilsExcel.writeData(file, "Sheet2", r, 8, "Failed")
            utilsExcel.fillRedColor(file, "Sheet2", r, 8)

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(3)

    driver.close()






