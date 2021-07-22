import ExcelUtils as utils
import openpyxl
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()

filePath = "C:\SeleniumPython\DataDrivenTesting\creds.xlsx"

rows = utils.getRowCount(filePath, "Sheet1")

for r in range(2, rows+1):
    username = utils.readData(filePath, "Sheet1", r, 1)
    password = utils.readData(filePath, "Sheet1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("submit").click()

    if driver.title == "Login: Mercury Tours":
        utils.writeData(filePath, "Sheet1", r, 3, "Login Success")
    else:
        utils.writeData(filePath, "Sheet1", r, 3, "Login Fail")

    driver.find_element_by_link_text("Home").click()

driver.quit()