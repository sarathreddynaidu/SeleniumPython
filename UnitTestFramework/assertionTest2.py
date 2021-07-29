# assertTrue - If result/value is True the test passes, if False the test fails
# assertFalse - If result/value is False the test passes, if True the test fails

import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test1(self):
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        driver.get("https://www.google.com")
        webPageTitle = driver.title  # Google
        self.assertTrue(webPageTitle == "Google", "Webpage titles are not same")
        self.assertFalse(webPageTitle == "Amazon", "Webpage titles are same")


if __name__ == "__main__":
    unittest.main()
