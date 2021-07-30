import unittest


class LoginTest(unittest.TestCase):

    def test_loginByEmail(self):
        print("Login by Email test")
        self.assertTrue(True)

    def test_loginByFB(self):
        print("Login by FB test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
