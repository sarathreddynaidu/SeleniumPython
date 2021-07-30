import unittest


class SignupTest(unittest.TestCase):

    def test_signupByEmail(self):
        print("Signup by Email test")
        self.assertTrue(True)

    def test_signupByFB(self):
        print("Signup by FB test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
