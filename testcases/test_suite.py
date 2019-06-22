import unittest
from testcases.catalog.catalog_testcases import Logcat
import HtmlTestRunner
import os

# Get all tests from the test classes

tc3 = unittest.TestLoader().loadTestsFromTestCase(Logcat)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc3])


dir = os.getcwd()
outfile = open(dir + "SmokeTestReport.html", "w")
runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')
runner.run(smokeTest)
