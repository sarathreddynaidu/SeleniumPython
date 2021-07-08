import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:/Users/sarat/Downloads"})

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=chromeOptions)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")

downloadFile = driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[3]/td[5]/a[1]")

downloadFile.click()

time.sleep(3)

driver.quit()
