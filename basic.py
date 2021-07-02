import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.seleniumframework.com/Practiceform/")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div/div[1]/div/p[4]/button").click()

time.sleep(5)

driver.close()
driver.quit()
