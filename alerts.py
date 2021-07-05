import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
alertButton = driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button")
time.sleep(2)

#Method 1
alertButton.click()
alert = driver.switch_to_alert() # or driver.switch_to.alert
time.sleep(2)
alert.accept() # Switches to alert window and clicks Ok
time.sleep(2)
alertButton.click()
time.sleep(2)
alert.dismiss() # Switches to alert window and clicks Cancel

# # Method 2
# alert = Alert(driver)
# alertButton.click() # clicks button which pops alert window
# time.sleep(2)
# alert.accept() # clicks Ok on the alert window
# time.sleep(2)
# alertButton.click()
# time.sleep(2)
# alert.dismiss() # clicks cancel on the alert window
# time.sleep(2)
