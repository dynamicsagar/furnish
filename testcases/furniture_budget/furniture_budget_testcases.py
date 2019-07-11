from pages.furniture_budget.furniture_budget_pages import FurnitureBudget
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Furniture(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)


    def test_01VerifyAddEdiFurnitureBudget(self):
        self.project_card = FurnitureBudget(self.driver)
        #self.project_card.loop()
        self.project_card.enterBudget()

    def test_02VerifyAddNegativeBudgetValue(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.enterNegativeValue()

    def test_03VerifyBudgetMet(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.budgetMet()

    def test_04VerifyBudgetOver(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.budgetOver()

    def test_05VerifyBudgetUnder(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.budgetUnder()

    def test_06VerifyCloseProjectDetailSummary(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.closeProjectLink()

    def test_07VerifyExpandProjectDetailSummary(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.expandProjectLink()

    '''def test_08VerifyProjectStatusChange1(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.projectStatus1()

    def test_09VerifyProjectStatusChange2(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.projectStatus2()

    def test_10VerifyProjectStatusChange3(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.projectStatus3()'''

    def test_11VerifyStargateLinkNavigation(self):
        self.project_card = FurnitureBudget(self.driver)
        self.project_card.clickStargateLink()


if __name__ == '__main__':
    unittest.main(verbosity=2)











