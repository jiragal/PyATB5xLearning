# Open the Url -www.ebay.com
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get al the prices
# Print all the titles and prices in the end.
#*********************************************************#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest,allure
import time
#*********************************************************#

@allure.title("scrape on ebay site for Mac mini")
@allure.description("Verify title and prices are scraping successfully")
@pytest.mark.positive
def test_scrape_ebay():
    path = 'https://www.ebay.com/'
    driver = webdriver.Firefox()
    driver.get(path)
    time.sleep(10)
    # Search for "Mac mini"
    search_box = driver.find_element(By.XPATH, "//input[@name='_nkw' and @title='Search']")
    search_box.send_keys("Mac mini")
    # Enter Key
    search_box.send_keys(Keys.RETURN)
    time.sleep(7)
    # Now we need to scrape "title" and "prices"
    title = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")  # Here "." meaning is it represents class
    prices = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    # Extract text and prices and print the results.
    for title, price in zip(title, prices):
        print(f"Title: {title.text}")
        print(f"Prices: {price.text}")
        print("*" * 50)
    time.sleep(7)
    driver.quit()