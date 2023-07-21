from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open the website
driver = webdriver.Chrome()
driver.get("https://www.example.com")

verify_button = self.driver.find_element_by_css_selector("div.btn.btn-primary")
verify_button.click()
time.sleep(4)

# Press the submit button to login
submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.click()