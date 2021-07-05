from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Find number of input boxes
inputBoxes = driver.find_elements(By.CLASS_NAME, "text_field")
print("Number of input boxes:", len(inputBoxes)) # 6

# Provide value into the text box
firstName = driver.find_element_by_id("RESULT_TextField-1")
lastName = driver.find_element(By.ID, "RESULT_TextField-2")
firstName.send_keys("Sarath Chandra Reddy")
lastName.send_keys("Naidu")

# Get status
status = firstName.is_enabled()
status1 = lastName.is_displayed()
print("Status of first name: ", status)
print("Status of second name: ", status1)

# driver.quit()
