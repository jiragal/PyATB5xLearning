import allure
import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType


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

    # # wait for the page to load completely
    WebDriverWait(driver,
                  10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='fromCity']")))

    #
    from_city = driver.find_element(By.ID, "fromCity")
    from_city.click()
    #Type "del" in the from From input box
    from_input =     driver.find_element(By.XPATH,
                        "//input[@placeholder='From']")
    from_input.send_keys("del")
    time.sleep(3)

    #Use the Down arrow key to select "Delhi" and press Enter
    from_input.send_keys(Keys.ARROW_DOWN)
    from_input.send_keys(Keys.ENTER)

    #Type "ban" in the To input box
    to_input=driver.find_element(By.XPATH,"//input[@placeholder='To']")
    to_input.send_keys("ban")
    time.sleep(3)
    to_input.send_keys(Keys.ARROW_DOWN)
    to_input.send_keys(Keys.ENTER)
    time.sleep(10)


    # to_city = driver.find_element(By.ID, "toCity")
    #
    # actions = ActionChains(driver=driver)
    # actions.move_to_element(from_city).click().send_keys("del").perform()
    # time.sleep(3)
    # actions.move_to_element(to_city).click().send_keys("ban").perform()
    # time.sleep(3)
    #
    # #Now click on "SEARCH" button
    # enter_key=driver.find_element(By.XPATH,"//a[normalize-space()='Search']")
    # enter_key.click()

    # time.sleep(10)
    # driver.quit()
