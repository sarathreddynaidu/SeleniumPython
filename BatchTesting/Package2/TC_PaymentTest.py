import unittest


class PaymentTest(unittest.TestCase):

    def test_paymentInUSD(self):
        print("Payment is USD test")
        self.assertTrue(True)

    def test_paymentInINR(self):
        print("Payment in INR test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()