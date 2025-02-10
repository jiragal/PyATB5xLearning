import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



# def test_practice():
#     driver=webdriver.Chrome()
#     driver.get("https://www.inmotionhosting.com/index.php")
#     sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
#     print(len(sliders))

def test_ibm_time_sheet():
    driver = webdriver.Edge()
    driver.get("https://time.ibm.com")
    driver.maximize_window()
    actions= ActionChains(driver)
    mywait = WebDriverWait(driver,10)
    mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='title']")))
    driver.implicitly_wait(5)
    enter_w3id = driver.find_element(By.XPATH, "//div[@id='credsDiv']")
    enter_w3id.click()
    driver.find_element(By.XPATH,"//*[@id = 'user-name-input']").send_keys("sanjivakumar.jiragal@ibm.com")
    driver.find_element(By.XPATH,"//input[@id='password-input']").send_keys("Sanjiva@2025?jan")
    driver.find_element(By.XPATH,"//button[@id='login-button']").click()
    max_attempts = 3
    for _ in range(max_attempts):
        try:
            element = WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/head/title"))
            )
            # Perform actions on the element
            break  # Exit the loop if successful

        except TimeoutException:
            continue  # Retry if a timeout occurs
    #Webdriver application related commands
    print(driver.title)
    print(driver.current_url)
    #print(driver.page_source)
    copy_from_pre_week = driver.find_element(By.XPATH,"//*[@id='btn-copy-prev-week']/parent::div")
    copy_from_pre_week.click()
    print("Display Status", copy_from_pre_week.is_displayed())

    ok_button = driver.find_element(By.XPATH,"//button[normalize-space()='Ok']")
    ok_button.click()
    WebDriverWait(driver,timeout=15).until(
        EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Claim item']"))
    )
    element = driver.find_element(By.XPATH, "//div[@class='mat-tooltip-trigger mat-tooltip-disabled'][normalize-space()='0']")
    actions.move_to_element(element).double_click().send_keys("9").perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)

    element1 = driver.find_element(By.XPATH,"//div[@class='mat-tooltip-trigger mat-tooltip-disabled']/ancestor::div[8]//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ds-clickable ds-text-align-center']")
    actions.move_to_element(element1).double_click().send_keys("9").perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    #Wensday
    element2 = driver.find_element(By.XPATH, "//div[2]/div/div/div/div[@col-id='sheet.hours.wed']")
    actions.move_to_element(element2).double_click().send_keys("9").perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    #Thursday
    element3 = driver.find_element(By.XPATH,"//div[2]/div/div/div/div[@col-id='sheet.hours.thu']")
    actions.move_to_element(element3).double_click().send_keys("9").perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    #Friday
    element4 = driver.find_element(By.XPATH,"//div[2]/div/div/div/div[@col-id ='sheet.hours.fri']")
    actions.move_to_element(element4).double_click().send_keys("9").perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    #Submit time hours
    save=driver.find_element(By.XPATH,"//button[@id='btn-timesheet-save']")
    save.click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@id='btn-timesheet-submit']").click()
    time.sleep(2)
    driver.close()
