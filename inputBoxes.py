from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Find number of input boxes
inputBoxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(inputBoxes)) # 6

# Provide value into the text box
driver.find_element_by_id("RESULT_TextField-1").send_keys("Sarath Chandra Reddy")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Naidu")

# driver.quit()
