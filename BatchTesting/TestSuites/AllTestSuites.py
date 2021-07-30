import unittest

from BatchTesting.Package1.TC_LoginTest import LoginTest
from BatchTesting.Package1.TC_SignUpTest import SignupTest
from BatchTesting.Package2.TC_PaymentTest import PaymentTest
from BatchTesting.Package2.TC_PaymentReturns import PaymentReturnsTest

# Get all tests from the above imported classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # tests from package1
# unittest.TextTestRunner().run(sanityTestSuite)

functionalTestSuite = unittest.TestSuite([tc3, tc4])  # tests from package2
# unittest.TextTestRunner().run(functionalTestSuite)

masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # tests from both packages
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)  # verbosity gives more details
