import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
dropDown = Select(element)
time.sleep(2)

# Select by visible text
dropDown.select_by_visible_text("Morning")
time.sleep(2)

# Select by index (index starts from zero)
dropDown.select_by_index(2)
time.sleep(2)

# Select by value (value attribute in html)
dropDown.select_by_value("Radio-2")
time.sleep(2)

allOptions = dropDown.options
# Number of options in the dropdown
print(len(allOptions))

# Capture all the options and print them as output
for option in allOptions:
    print(option.text)
