import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME, "a")

# Number of links
print("Links in this page: ", len(links))

# Display all the links
for link in links:
    print(link.text)

# Click on specific link using link text and partial link text
time.sleep(2)
driver.find_element(By.LINK_TEXT, "REGISTER").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "SIGN").click()
