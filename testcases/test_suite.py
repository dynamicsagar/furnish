import unittest
from testcases.Dashboard.project_dashboard_ui_functionality.dashboard_ui_functionality import dashboardCases
from testcases.filter_bucket.bulk_and_view_type import Bucket
from testcases.furniture_budget.furniture_budget_testcases import Furniture
from testcases.global_catalog.global_catalog_testcases import globalCatalog
from testcases.login_logout.login_logout_testcases import LoginTests
from testcases.add_remove_products.add_remove_products_testcses import AddRemove
from testcases.catalog.catalog_testcases import Logcat

# Get all tests from the test classes

tc7 = unittest.TestLoader().loadTestsFromTestCase(Bucket)
tc1 = unittest.TestLoader().loadTestsFromTestCase(dashboardCases)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(globalCatalog)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Furniture)
tc6 = unittest.TestLoader().loadTestsFromTestCase(AddRemove)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Logcat)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc3, tc1, tc2, tc7, tc4, tc5, tc6])


unittest.TextTestRunner(verbosity=2).run(smokeTest)
