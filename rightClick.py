import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

time.sleep(2)

rightClickButton = driver.find_element(By.XPATH, "//*[@id='authentication']/span")

actions = ActionChains(driver)

# right click on the right click button
actions.context_click(rightClickButton).perform()

time.sleep(2)
driver.quit()
