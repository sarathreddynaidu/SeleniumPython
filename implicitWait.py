from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

userName = driver.find_element_by_name("userName")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_name("submit")

userName.send_keys("pythonselenium")
password.send_keys("pythonselenium")
submit.click()

driver.quit()