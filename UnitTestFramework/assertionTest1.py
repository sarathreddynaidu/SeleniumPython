# assertEqual - If both parameters are equal the test passes, if not equal the test fails
# assertNotEqual - If both parameters are not equal the test passes, if equal the test fails

import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test1(self):
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        driver.get("https://www.google.com")
        webPageTitle = driver.title  # Google
        self.assertEqual(webPageTitle, "Google", "Webpage titles are not same")
        self.assertNotEqual(webPageTitle, "Amazon", "Webpage titles are same")


if __name__ == "__main__":
    unittest.main()
