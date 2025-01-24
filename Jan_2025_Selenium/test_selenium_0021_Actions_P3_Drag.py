import time

import pytest, allure
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options


@allure.title("Actions P3")
@allure.description("Verify user is able to drag ")
def test_verify_action_mouse_drag():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Element to hold
    element_to_hold = driver.find_element(By.ID, "draggable")

    # KEY_DOWN
    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(10)
    driver.quit()
