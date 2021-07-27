from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://www.google.com")

#Method1
filePath = "C:\SeleniumPython\ScreenShots\googlepage1.jpg"
driver.save_screenshot(filePath)

#Method2 - this only accepts png
# filePath = "C:\SeleniumPython\ScreenShots\googlepage2.png"
# driver.get_screenshot_as_file(filePath)

driver.quit()