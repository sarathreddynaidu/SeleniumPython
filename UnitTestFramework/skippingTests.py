# skip test - add @unittest.SkipTest decorator above test function to skip that test
# skip test with reason - add @unittest.skip("reason") decorator above test function to skip that test with a reason message
# skip test with condition - add @unittest.skipIf(condition, "message") decorator above test function to skip that test if the condition is true

import unittest


class APPTest(unittest.TestCase):

    def test_login(self):
        print("Login test")

    @unittest.skipIf(1 == 1, "same numbers are not equal")
    def test_search(self):
        print("Search test")

    @unittest.SkipTest
    def test_advance_search(self):
        print("Advance search test")

    @unittest.skip("Not working so skipped it")
    def test_click(self):
        print("Click test")

    @unittest.SkipTest
    def test_input(self):
        print("Input test")

    def test_logout(self):
        print("Logout test")


if __name__ == "__main__":
    unittest.main()
