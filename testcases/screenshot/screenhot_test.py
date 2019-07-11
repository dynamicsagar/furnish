from pages.screenshot.screenhot_page import ScreenshotPage
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ScreenshotTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def ObjectSetup(self):
        self.screen = ScreenshotPage(self.driver)

    def test_01VerifyHomeScreen(self):
        self.screen.Home()

    def test_02ProjectDetailScreen(self):
        self.screen.ProjectDetailScreen()

    def test_03AssignmentScreen(self):
        self.screen.AssignmentScreen()

    def test_04AssignmentScreenEditScreen(self):
        self.screen.AssignmentScreenNewRoom()

    def test_05AssignmentScreenRemoveProductPopScreen(self):
        self.screen.AssignmentScreenRemoveProduct()

    def test_06ViewRoomScreen(self):
        self.screen.ViewByRoomScreen()

    def test_07ViewRoomEditScreen(self):
        self.screen.ViewByRoomEditScreenPopUP()

    def test_08ViewRoomNewProductScreen(self):
        self.screen.ViewByRoomAssignNewProductScreen()

    def test_09VerifyCatalogScreen(self):
        self.screen.CatalogScreen()

    def test_10VerifyCatalogDetailScreen(self):
        self.screen.CatalogDetailScreen()
