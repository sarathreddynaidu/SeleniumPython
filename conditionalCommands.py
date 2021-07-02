from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

userName = driver.find_element_by_name("userName")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_name("submit")

print("Status of user name displayed is" , userName.is_displayed())
print("Status of user name enabled is" , userName.is_enabled())
print("Status of password displayed is" , password.is_displayed())
print("Status of password enabled is" , password.is_enabled())

userName.send_keys("pythonselenium")
password.send_keys("pythonselenium")
submit.click()

driver.find_element_by_link_text("Flights").click()

roundTripRadio = driver.find_element_by_css_selector("input[value=roundtrip]")
oneWayRadio = driver.find_element_by_css_selector("input[value=oneway]")

print("Status of round trip radio button is", roundTripRadio.is_selected())
print("Status of one way radio button is", oneWayRadio.is_selected())

driver.quit()