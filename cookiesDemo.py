from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://www.amazon.com")
driver.maximize_window()

print("Default Cookies")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(cookies)  # Prints all the cookies as dict
print(len(cookies))  # Print number of cookies

# Adding new cookie to the browser
cookie = {"name": "MyCookie", "value": "123"}
driver.add_cookie(cookie)
print("Adding Cookie")
cookies = driver.get_cookies()  # Do this after adding/deleting cookies
print(cookies)
print(len(cookies))

# Deleting a cookie
driver.delete_cookie("MyCookie")  # Pass the name of the cookie from the dict file
print("Deleting Cookie")
cookies = driver.get_cookies()  # Do this after adding/deleting cookies
print(cookies)
print(len(cookies))

driver.quit()
