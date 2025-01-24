# mouse action program
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Actions mouse P2")
@allure.description("Verify user is able to perform 'mouse back' operation ")
@pytest.mark.systemtesting
def test_verify_action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    atag=driver.find_element(By.XPATH," //a[contains(@id,'click')]")
    atag.click()
    time.sleep(5)
    #From this point we need to right click on mouse and then click "Back"
    #Current-Page: https://awesomeqa.com/selenium/resultPage.html

    action_builder = ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()
    time.sleep(10)
    driver.quit()


