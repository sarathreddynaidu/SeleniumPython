from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.implicitly_wait(10)

# To check status of radio button

maleButton = driver.find_element_by_id("RESULT_RadioButton-7_0")
femaleButton = driver.find_element_by_id("RESULT_RadioButton-7_1")

maleButtonStatus = maleButton.is_selected()
femaleButtonStatus = femaleButton.is_selected()

print("Status of male button: ", maleButtonStatus)
print("Status of female button: ", femaleButtonStatus)

# To click button

maleButton.click()
print("After clicking male button...")
print("Status of male button: ", maleButtonStatus)

# Selecting radio buttons

sunday = driver.find_element_by_id("RESULT_CheckBox-8_0")
saturday = driver.find_element_by_id("RESULT_CheckBox-8_6")

sundayStatus = sunday.is_selected()
saturdayStatus = saturday.is_selected()

print("Status of sunday button", sundayStatus)
print("Status of saturday button", saturdayStatus)

sunday.click()

print("After clicking sunday...")
print("Status of sunday button", sundayStatus)