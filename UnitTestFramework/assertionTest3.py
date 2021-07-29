# assertIsNone - If result/value is None the test passes, if Not None the test fails
# assertIsNotNone - If result/value is Not None the test passes, if Not None the test fails

import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test1(self):
        driver = None
        self.assertIsNone(driver, "Driver is Not None")
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        self.assertIsNotNone(driver, "Driver is None")


if __name__ == "__main__":
    unittest.main()
