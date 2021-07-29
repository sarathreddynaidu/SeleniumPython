# assertIn - If first element is present in the second element test passes, otherwise test fails
# assertNotIn - If first element is not present in the second element test passes, otherwise test fails
# These two are used to verify presence of a value in a list, tuple, set, and dict

import unittest


class Test(unittest.TestCase):

    def test1(self):
        fav = ["Python", "Selenium"]
        self.assertIn("Python", fav)
        self.assertNotIn("Java", fav)


if __name__ == "__main__":
    unittest.main()
