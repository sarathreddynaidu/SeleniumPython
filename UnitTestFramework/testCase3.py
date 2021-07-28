# setup - this will execute multiple times before executing every test method
# tearDown - this will execute multiple times after executing every test method
# setupClass - this will execute once before the class
# tearDownClass - this will execute once after the class
# setUpModule - this will execute once before the module (before any class or method)
# tearDownModule - this will execute once after the module

import unittest

def setUpModule():
    print("SetUpModule")

def tearDownModule():
    print("TearDownModule")


class AppTesting(unittest.TestCase):

    def test_search(self):
        print("Search test")

    def test_advance_search(self):
        print("Advance search test")

    def test_click(self):
        print("Click test")

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open app")

    @classmethod
    def tearDownClass(cls):
        print("Close app")


if __name__ == "__main__":
    unittest.main()