import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(3)

sourceElement = driver.find_element(By.ID, "box7")
targetElement = driver.find_element(By.ID, "box107")

actions = ActionChains(driver)

actions.drag_and_drop(sourceElement, targetElement).perform()

time.sleep(3)
driver.quit()
