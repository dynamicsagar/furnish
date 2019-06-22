from pages.add_remove_product.add_remove_product_page import addRemoveProducts
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddRemove(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.addremove = addRemoveProducts(self.driver)

    def test_01VerifyAddProduct(self):
        self.log.info("*#" * 20)
        self.log.info("test_01VerifyAddProduct -- Add product using add assignment link")
        self.log.info("*#" * 20)
        self.addremove.add()

    def test_02VerifyCountOfProducts(self):
        self.log.info("*#" * 20)
        self.log.info("test_02VerifyCountOfProducts --- Count of product after adding the product")
        self.log.info("*#" * 20)
        self.addremove.productAddedViewByType()

    def test_03VerifySubtotal(self):
        self.log.info("*#" * 20)
        self.log.info("test_03VerifySubtotal --- Verify subtotal after adding some quantity")
        self.log.info("*#" * 20)
        self.addremove.addRoomAssignment()

    def test_05VerifyEditExistingTabSearchFunctionalityRelevantData(self):
        self.log.info("*#" * 20)
        self.log.info("test_05VerifyEditExistingTabSearchFunctionalityRelevantData ==== Search functionality in edit address window with relevant data")
        self.log.info("*#" * 20)
        self.addremove.searchRelevantKeyword()

    def test_06VerifyEditExistingTabSearchFunctionalityIrrelevantData(self):
        self.log.info("*#" * 20)
        self.log.info("test_06VerifyEditExistingTabSearchFunctionalityIrrelevantData ---- Search functionality in edit address window with irrelevant data")
        self.log.info("*#" * 20)
        self.addremove.searchIrrelevantKeyword()

    def test_07VerifyFloorDropdownFilterFunctionality(self):
        self.log.info("*#" * 20)
        self.log.info("Select floor from the dropdown and verify result accordingly")
        self.log.info("*#" * 20)
        self.addremove.floorSelection()

    def test_08VerifyFloorDropdownFilterFunctionalityNoRoomResult(self):
        self.log.info("*#" * 20)
        self.log.info("Select floor from the dropdown and verify result message when no data avaialble")
        self.log.info("*#" * 20)
        self.addremove.floorWithoutDateSelection()

    def test_09VerifyCancelButtonFunctionality(self):
        self.log.info("*#" * 20)
        self.log.info("Clicking on cancel button wont impact")
        self.log.info("*#" * 20)
        self.addremove.addEditButtonCancelFunctionality()

    def test_10VerifyIncreaseQuantityApplyChanges(self):
        self.addremove = addRemoveProducts(self.driver)
        self.addremove.quantityIncrease()

    def test_11VerifyDecreaseQuantityApplyChanges(self):
        self.addremove = addRemoveProducts(self.driver)
        self.addremove.quantityDecrease()

    def test_12VerifyFailureMsgEnteringIrrelevantQuantity(self):
        self.log.info('Failure Msg entering irrelevant data')
        self.addremove.enterIrrelevantDataInQuantity()

    def test_13VerifyChangesAfterRemovingTheRoom(self):
        self.addremove = addRemoveProducts(self.driver)
        self.addremove.deleteRoomChangesApply()

    def test_14VerifyBinButtonFunctionality(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info("*#" * 20)
        self.log.info("*#" * 20)
        self.addremove.binButton()

    def test_15VerifyCloseButtonFunctionality(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info("close button functionality")
        self.log.info("*#" * 20)
        self.addremove.closeButton()

    def test_16VerifyLinkToTheProductDetailsfunctionality(self):
        self.log.info("*#" * 20)
        self.log.info('Link to the product details functionality - User should get redirected to that product detail page of that product in a new tab')
        self.log.info("*#" * 20)
        self.addremove.productLinkInEditBox()

    def test_17VerifyRemoveModelBoxText(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('Removing a product from product detail page - RemoveModelBoxText')
        self.log.info("*#" * 20)
        self.addremove.removeProductText()

    def test_18VerifyCancelButtonClickOnRemoveModalBox(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('Removing a product from product detail page - Click Cancel Button On Remove ModalBox')
        self.log.info("*#" * 20)
        self.addremove.cancelButton()

    def test_19RemoveProduct(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('Removing a product from product detail page - RemoveProduct')
        self.log.info("*#" * 20)
        self.addremove.remove()


    def test_20AssignNewRoomSearch(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('Assign to new rooms Tab - Search Functionality')
        self.log.info("*#" * 20)
        self.addremove.AssignToNewRoom_searchFunctionality()


    def test_21AssignNewRoomSearchWithoutData(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('Assign to new rooms Tab - Search Functionality')
        self.log.info("*#" * 20)
        self.addremove.AssignToNewRoom_IrreleavantSearchFunctionality()


    def test_22AssignNewRoomDropDownFilterFloor(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('# Assign to new rooms Tab - Floor drop-down filter Functionality')
        self.log.info("*#" * 20)
        self.addremove.AssignToNewRoom_FloorFilterDropDown()


    def test_23ProductDetail_ProductDropDownFilterSelectUnassigned(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('# Product Detail Screen -  Product dropdown filter- Select Unassigned')
        self.log.info("*#" * 20)
        self.addremove.ProductDetailScreen_ProductDropdownUnassigned()


    def test_24ProductDetail_ProductDropDownFilterSelectAssigned(self):
        self.addremove = addRemoveProducts(self.driver)
        self.log.info("*#" * 20)
        self.log.info('# # Product Detail Screen -  Product dropdown filter- Select Assigned')
        self.log.info("*#" * 20)
        self.addremove.ProductDetailScreen_ProductDropdownAssigned()





