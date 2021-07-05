import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
# print(driver.current_window_handle) # handle value for the current window

driver.find_element(By.LINK_TEXT, "click").click()
windowHandles = driver.window_handles
print(windowHandles) # returns array of all the windows handle values

# Print each window handle value:
for handleValue in windowHandles:
    driver.switch_to.window(handleValue)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() # closes that particular window

time.sleep(5)

driver.quit()