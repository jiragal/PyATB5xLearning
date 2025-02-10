import allure,time
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Spice-Jet Automation")
@allure.description("Verify Make My Trip Automation by using Action Classes")
@pytest.mark.systemtestng
def test_verify_spicejet_website():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    # Navigate to the spicejet
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    # # Wait for page to load
    time.sleep(5)
    # #Action class instance
    actions = ActionChains(driver=driver)
    # #
    # # #Enter del in the "From" search box
    from_city=driver.find_element(By.XPATH,
                                  "//input[@data-focusvisible-polyfill='true']")
    actions.move_to_element(from_city).click().send_keys("DEL").pause(2).send_keys(Keys.ENTER).perform()
    # time.sleep(10)
