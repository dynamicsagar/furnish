import unittest
from testcases.catalog.catalog_testcases import Logcat

# Get all tests from the test classes

tc3 = unittest.TestLoader().loadTestsFromTestCase(Logcat)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc3])


unittest.TextTestRunner(verbosity=2).run(smokeTest)
