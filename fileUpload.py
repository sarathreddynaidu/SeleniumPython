import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame("frame-one1434677811")

chooseFile = driver.find_element(By.ID, "RESULT_FileUpload-10")

chooseFile.send_keys("C:/Users/sarat/Downloads/dummy.pdf")

time.sleep(3)
driver.quit()