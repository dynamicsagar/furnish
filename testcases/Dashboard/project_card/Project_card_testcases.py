from pages.Dashboard.Project_card_contents.Project_card_pages import projectcard
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProjectCard(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)


    def test_01VerifyAddEdiFurnitureBudget(self):
        self.project_card = projectcard(self.driver)
        self.project_card.loop()
        self.project_card.enterBudget()

    def test_02VerifyAddNegativeBudgetValue(self):
        self.project_card = projectcard(self.driver)
        self.project_card.enterNegativeValue()

    def test_03VerifyBudgetMet(self):
        self.project_card = projectcard(self.driver)
        self.project_card.budgetMet()

    def test_04VerifyBudgetOver(self):
        self.project_card = projectcard(self.driver)
        self.project_card.budgetOver()

    def test_05VerifyBudgetUnder(self):
        self.project_card = projectcard(self.driver)
        self.project_card.budgetUnder()

    def test_06VerifyCloseProjectDetailSummary(self):
        self.project_card = projectcard(self.driver)
        self.project_card.closeProjectLink()

    def test_07VerifyExpandProjectDetailSummary(self):
        self.project_card = projectcard(self.driver)
        self.project_card.closeProjectLink()

    '''def test_05VerifyProjectStatus(self):
        self.project_card = projectcard(self.driver)
        self.project_card.projectStage()


    def test_06VerifyProjectStatusChange1(self):
        self.project_card = projectcard(self.driver)
        self.project_card.projectStageChange1()
        assert True

    def test_07VerifyProjectStatusChange2(self):
        self.project_card = projectcard(self.driver)
        self.project_card.projectStageChange2()
        assert True

    def test_08VerifyProjectStatusChange3(self):
        self.project_card = projectcard(self.driver)
        self.project_card.projectStageChange3()
        assert True'''

    def test_08VerifyStargateLinkNavigation(self):
        self.project_card = projectcard(self.driver)
        self.project_card.clickStargateLink()












