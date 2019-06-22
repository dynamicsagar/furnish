from pages.catalog.catalog_pages import CatalogPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Logcat(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def ObjectSetup(self):
        self.ca = CatalogPages(self.driver)

    @pytest.mark.run(order=1)
    def test_01VerifyAccessCatalogFromAddMoreProductButton(self):
        self.ca.accessCatalogPage()

    def test_02VerifyAccessCatalogPageFromShopForMoreLink(self):
        self.ca.accessCatalogPageSearchFromProduct()

    def test_03VerifySubmenuNavigationFromHome(self):
        self.ca.navigateHomePage()

    def test_04VerifyLogoutFromCatalogScreen(self):
        self.ca.clickLogout()

