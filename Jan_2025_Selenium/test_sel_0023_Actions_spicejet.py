import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.title("Spice-Jet Automation")
@allure.description("Verify Make My Trip Automation by using Action Classes")
@pytest.mark.systemtestng
def test_verify_spicejet_website():
    # chrome_options=webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome()
    #Navigate to the spicejet
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    # Wait for page to load
    time.sleep(3)
    #Action class instance
    actions = ActionChains(driver=driver)

    #Enter del in the "From" search box
    from_city=driver.find_element(By.XPATH,"//input[contains(@placeholder,'From')]")
    actions.move_to_element(from_city).click().send_keys("DEL").pause(2).send_keys(Keys.ENTER).perform()
    time.sleep(10)






