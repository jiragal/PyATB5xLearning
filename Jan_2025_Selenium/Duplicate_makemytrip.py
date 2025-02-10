import allure
import pytest
import time

from pip._internal.utils import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime


@allure.title("Make My Trip Automation")
@allure.description("Verify Make My Trip Automation by using Action Classes")
@pytest.mark.systemtesting
def test_verify_action_make_my_trip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    # Webdriverwait() it is equivalent to time.sleep()
    WebDriverWait(driver=driver, timeout=7).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal' and @class='commonModal__close']")))

    driver.find_element(By.XPATH, "//span[@data-cy='closeModal' and @class='commonModal__close']").click()
    #time.sleep(10)
    # # wait for the page to load completely
    WebDriverWait(driver,
                  10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='fromCity']")))

    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("del").perform()
    time.sleep(2)
    actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

    to_city = driver.find_element(By.ID, "toCity")
    actions.move_to_element(to_city).click().send_keys("Ban").perform()
    time.sleep(2)
    f= actions.move_to_element(to_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).key_down(Keys.RETURN)
    f.click()
    time.sleep(10)

    #Select the current Date
    current_date=datetime.now().day
    calendar_date_xpath = f"//div[contains(@class, 'DayPicker-Day') and not(contains(@class, 'DayPicker-Day--disabled'))]//p[text()='{current_date}']"
    date_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, calendar_date_xpath)))
    date_element.click()
    time.sleep(5)

    # #Now user will click on "SEARCH" button
    search_button = driver.find_element(By.XPATH, "//a[contains(@class, 'primaryBtn')]")
    search_button.click()
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listingCard')]")))
    #
    # # #wait for the results to load
    # time.sleep(10)
    driver.quit()
