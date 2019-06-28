import utilities.custom_logger as cl
from pages.view_by_room.view_by_room import ViewByRoom
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ViewRoom(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def ObjectSetup(self):
        self.room = ViewByRoom(self.driver)

    def test_01VerifyRoomCountFromViewByRoom(self):
        self.room.AllRoomCount()

    def test_02VerifyAddProductRoomInViewRoomWithoutAssignProduct(self):
        self.room.ProductAddInRoom()

    def test_03VerifyCancelButtonInViewRoomWithoutAssignProduct(self):
        self.room.ProductRoomCancelButton()

    def test_04VerifyCloseButtonInViewRoomWithoutAssignProduct(self):
        self.room.ProductRoomCloseButton()

    def test_05VerifySearchProductWithProductNameInViewRoomWithoutAssignProduct(self):
        self.room.SearchProductUsingProductName()

    def test_06VerifyClickOnProductNameNavigation(self):
        self.room.ClickProductName()

    def test_07VerifyIrrelevantSearchInViewRoomWithoutAssignProduct(self):
        self.room.IrrelevantProductNameSearch()

    def test_08VerifyEditExistingTabEmptyMessage(self):
        self.room.EmptyMessageOnEditExistingTab()

    def test_09VerifySelectViewRoomWithProducts(self):
        self.room.SelectViewRoomWithProduct()

    def test_10VerifyProductQuantityByIncreasing(self):
        self.room.quantityIncrease()

    def test_11VerifyProductQuantityByDecrease(self):
        self.room.quantityDecrease()

    def test_12VerifyMessageEnteringIrrelevantQuantity(self):
        self.room.enterIrrelevantDataInQuantity()

    def test_13VerifyProductDeleteButtonFunctionality(self):
        self.room.deleteRoomChangesApply()

    def test_14VerifyCancelButtonEditExistingTab(self):
        self.room.EditExistingCancelButton()

