import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# web-driver conditional types
search_store = driver.find_element(By.XPATH, "//*[@id='small-searchterms']")  # The search_store contains web_elements
print("Display Status: ", search_store.is_displayed())  # True or False
print("Is Enabled: ", search_store.is_enabled())

#is_selected()  used mainly for radio buttons/checkboxes like it is selected or not
male_radio_button = driver.find_element(By.CSS_SELECTOR, "span[class='male']")
fm_rd = driver.find_element(By.XPATH, "//span[@class='female']")

print("Male_Radio_Button_Selected: ", male_radio_button.is_selected())
print("female_radio_button_selected: ", fm_rd.is_selected())

driver.quit()

