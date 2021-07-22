from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("file:///C:/SeleniumPython/table.html")

rows = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
columns = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")

rowsCount = len(rows)
columnsCount = len(columns)

print(rowsCount)
print(columnsCount)

print("Product", "  Article", " Price")

for row in range(2, rowsCount+1):
    for column in range(1, columnsCount+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(row)+"]/td["+str(column)+"]").text
        print(value, end="     ")
    print()

driver.quit()
