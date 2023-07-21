from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc 

driver = uc.Chrome()

rf = open('url-list1.txt', 'r')
wf = open('result1.txt', 'w')

i = 4
for url in rf:
    i = i + 1
    driver.get(url)
    # elems = driver.find_elements(By.CSS_SELECTOR, "div.product-briefing")
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-briefing")))
    wf.write(elem.get_attribute("innerHTML"))
    assert "No results found." not in driver.page_source

rf.close()
wf.close()

driver.close()
