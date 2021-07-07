import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
time.sleep(2)

clickButton = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

# double click on click button
actions.double_click(clickButton).perform()

time.sleep(3)
driver.quit()
