import allure, pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#For Keyboard we need to use "ActionChains"
@allure.title("Actions P1")
@allure.description("Verify Actions p1")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(7)

    fidrst_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    actions=ActionChains(driver=driver)
    (actions.key_down(Keys.SHIFT).
     send_keys_to_element(fidrst_name,"the testing academy ")
     .key_up(Keys.SHIFT)
     .perform())

    time.sleep(10)
    driver.quit()