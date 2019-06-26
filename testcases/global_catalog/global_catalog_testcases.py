from pages.global_catalog.global_catalog_pages import GlobalCatalog
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class globalCatalog(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_01VerifyAccessTheGlobalCatalogPage(self):
        self.gc = GlobalCatalog(self.driver)
        result = self.gc.catalogPage()
        return result  == True

    def test_02VerifyIndicateloggedinUser(self):
        self.gc = GlobalCatalog(self.driver)
        result = self.gc.userProfilePicture()
        assert result == True

    def test_03_01VerifyFilterPresent(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterLabel()
        self.gc.availabilityLabel()
        self.gc.collectionFilter()
        self.gc.regionFilter()
        self.gc.typeFilter()
        self.gc.subTypeFilter()
        self.gc.manufactureFilter()
        self.gc.vendorFilter()
        self.gc.materialFilter()

    def test_03_02VerifySeeMorelink(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.checkSeeMorelink()

    def test_03_03VerifyFilterAppliedDisplay(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.applyFilter()

    def test_03_04VerifyAppliedFilterResults(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.verifyAppliedFilterDetailPage()

    def test_04VerifySearchBoxSearching(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.searchBox()

    def test_05VerifySearchUsingSKU(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.skuSearch()

    def test_06VerifyBulkTag(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterTagVerification()

    def test_07VerifyBulk2Tag(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterTagBulk2()

    def test_08VerifyCustomTag(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterTagCustom()

    def test_09VerifyPacificCoreTag(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterTagPacificCore()

    def test_10VerifyPhoenixTag(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.filterTagPhoenix()

    def test_11VerifySortByLowest(self):
        self.gc = GlobalCatalog(self.driver)
        result = self.gc.clickSortLowestDropdown()
        assert result == True

    def test_12VerifySortByHighest(self):
        self.gc = GlobalCatalog(self.driver)
        result = self.gc.sortHighest()
        assert result == True

    def test_13VerifyHomeButton(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.clickHomeSubMenu()

    def test_14VerifyHomeButtonDetailPage(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.clickHomeProductDetail()

    def test_15VerifySpecificationDetailPage(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.checkSpecButtonDetailPage()

    def test_16VerifyGlobalCatalogLogout(self):
        self.gc = GlobalCatalog(self.driver)
        self.gc.clickLogout()





















