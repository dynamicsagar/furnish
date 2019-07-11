from pages.Dashboard.project_Dashboard_ui_functionality.dashboard_ui_functionality import dashboard
import utilities.custom_logger as cl
import unittest
import pytest
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class dashboardCases(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_01VerifyOpeningText(self):
        self.dash = dashboard(self.driver)
        self.dash.openingText()

    def test_02VerifyFloorCountText(self):
        self.dash = dashboard(self.driver)
        self.dash.floorCount()

    def test_03VerifyProgressBar(self):
        self.dash = dashboard(self.driver)
        result = self.dash.bar()
        assert result == True

    def test_04VerifyBudgetAllocatedText(self):
        self.dash = dashboard(self.driver)
        self.dash.budgetAllocated()

    def test_05VerifyEstimatedTotalText(self):
        self.dash = dashboard(self.driver)
        self.dash.estimatedTotal()

    '''def test_06VerifyProjectStatus(self):
        self.dash = dashboard(self.driver)
        result = self.dash.projectStatus()
        assert result == True'''

    def test_07VerifyUserDetailScreenOpen(self):
        self.dash = dashboard(self.driver)
        self.dash.projectCardToProjectDetail()

    def test_08VerifyPagination(self):
        self.dash = dashboard(self.driver)
        result = self.dash.clickPagination()
        assert result == True

    def test_09VerifyGlobalCatalog(self):
        self.dash = dashboard(self.driver)
        result = self.dash.catalogPage()
        return result == True

    def test_10VerifyLinkNavigation(self):
        self.dash = dashboard(self.driver)
        result = self.dash.linkNavigation()
        assert result == True


