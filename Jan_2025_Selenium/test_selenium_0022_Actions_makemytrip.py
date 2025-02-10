from selenium import webdriver
import time, pytest, allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime


def test_makemytrip_search():
    driver = webdriver.Chrome()
    try:
        #Initiate the webdriver
        #driver = webdriver.Chrome()

        # Open MakeMyTrip website
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()

        #Wait for the page to load
        time.sleep(5)

        #Close any pop-ups if they appear(optional)
        try:
            driver.find_element(By.XPATH, "//span[@data-cy='closeModal' and @class='commonModal__close']").click()

        except:
            pass

        #Click on the "From" input field
        from_input = driver.find_element(By.ID,"fromCity")
        actions = ActionChains(driver)
        actions.move_to_element(from_input).click().send_keys("del").perform()
        actions.move_to_element(from_input).key_down(Keys.ARROW_DOWN).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
        time.sleep(3)

        #Click on the "To" input field
        to_input = driver.find_element(By.ID, "toCity")
        to_input.click()
        to_search=driver.find_element(By.CSS_SELECTOR,"input[placeholder='To']")
        actions.move_to_element(to_input).send_keys("bengaluru").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

        # Select the current date
        current_date = datetime.now().strftime("%a %b %d %Y")  # Format: "Wed Jan 29 2025"
        date_picker = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{current_date}']")))

        date_picker.click()

        # Click the search button
        search_button = driver.find_element(By.CSS_SELECTOR, "a[class*='primaryBtn']")
        search_button.click()
        # Wait for the search results to load
        time.sleep(10)

    finally:
        #close the browser
        driver.quit()


