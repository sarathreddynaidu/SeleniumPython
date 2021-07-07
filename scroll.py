import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
time.sleep(2)

# scroll by pixel (0 - min, 1000 - max)
driver.execute_script("window.scrollBy(0, 1000)", "")

driver.get(driver.current_url)
time.sleep(2)
indiaFlag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")

# Scroll until element found
driver.execute_script("arguments[0].scrollIntoView();", indiaFlag)

driver.get(driver.current_url)
time.sleep(2)

# Scroll to end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

driver.quit()