# assertGreater - If first value is greater than second value test passes, otherwise test fails
# assertGreaterEqual - If first value is greater than or equal to second value test passes, otherwise test fails
# assertLess - If first value is less than second value test passes, otherwise test fails
# assertLessEqual - If first value is less than or equal to second value test passes, otherwise test fails

import unittest


class Test(unittest.TestCase):

    def test1(self):
        self.assertGreater(100, 10)
        self.assertGreaterEqual(100, 10)
        self.assertGreaterEqual(100, 100)
        self.assertLess(10, 100)
        self.assertLessEqual(10, 100)
        self.assertLessEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
