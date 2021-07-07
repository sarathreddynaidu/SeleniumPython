import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
loginButton = driver.find_element(By.ID, "btnLogin")
time.sleep(2)

username.send_keys("Admin")
password.send_keys("admin123")
time.sleep(2)
loginButton.click()
time.sleep(2)

adminTab = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
userManagementTab = driver.find_element(By.ID, "menu_admin_UserManagement")
userTab = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

actions = ActionChains(driver)

# hover on admin, hover on user management then click on user
actions.move_to_element(adminTab).move_to_element(userManagementTab).move_to_element(userTab).click().perform()

time.sleep(2)
driver.quit()
