import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "FRAMES").click()
time.sleep(2)

driver.switch_to.frame("packageListFrame") # switches to first frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content() # switch back to default page before switching frames
time.sleep(2)

driver.switch_to.frame("packageFrame") # switches to second frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content() # switch back to default page before switching frames
time.sleep(2)

driver.switch_to.frame("classFrame") # switches to third frame
driver.find_element(By.LINK_TEXT, "DEPRECATED").click()
time.sleep(2)
