import time
from base.selenium_driver import SeleniumDriver
from pages.add_remove_product.add_remove_product_page import addRemoveProducts


class FilterBucket(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _total_count = "//div[@id='root']/div/div[3]/div/div/div/div[2]/ul/li[8]"
    _element_name = "//p[contains(text(),'1 Milk - P1')]"
    _next = "//li[contains(text(),'Next')]"

    # Finding specific post using loop
    def loop(self):
        time.sleep(15)
        self.waitForElement(self._total_count)
        count = int(self.getText(self._total_count))
        print(count)
        for i in range(count):
            time.sleep(2)
            element_name = "1 Milk - P1"
            textname = self.getText(self._element_name)
            if element_name == textname:
                break
            else:
                next_link = self.getElement(self._next)
                next_link.click()
        self.elementClick(self._element_name)

    # Remove the product after adding into product detail view.
    def RemoveAddedProduct(self):
        self.add = addRemoveProducts(self.driver)
        self.add.remove()


    '''
    Test case :
    Steps:
    1. Login to app
    2. Loop the app to reach to specific product
    3. Click on the product
    4. Click add product button
    5. Select filter 
    6. Click first product after selecting the filter
    7. Click add product
    8. Click submenu
    
    Verify --
    1. View by type is having the same filter as we have selected o the catalog page. 
    2. Verify Bulk copy button should have selected filter text.
    
    '''


    # CATALOG
    _click_accessory_filter = "//label[contains(text(),'Accessory')]"
    _click_furniture_filter = "//label[contains(text(),'Furniture')]"
    _click_office_furniture_filter = "//label[contains(text(),'Office furniture')]"
    _click_ops_asset_filter = "//label[contains(text(),'Ops asset')]"
    _add_to_project = "//span[contains(text(),'Add to project')]"
    _click_sub_menu = "//span[3][contains(text(),'1 Milk - P1')]"
    _view_by_type_accessory_filter = "//span[contains(text(),'Accessory')]"
    _view_by_type_furniture_filter = "//span[contains(text(),'Furniture')]"
    _view_by_type_office_furniture_filter = "//span[contains(text(),'Office Furniture')]"
    _view_by_type_ops_asset_filter = "//span[contains(text(),'Ops Asset')]"
    _click_bulk_copy_button = "//span[contains(text(),'Bulk copy SKUs')]"
    _bulk_copy_list = "//body//li[1]"


    # TC 01 - Accessory added in View by type filter bucket
    def AddingAccessoryProduct_VerifyAddedInViewByType(self):
        self.loop()
        self.add = addRemoveProducts(self.driver)
        time.sleep(2)
        self.add.addProduct()
        time.sleep(2)
        self.elementClick(self._click_accessory_filter)
        time.sleep(2)
        self.add.clickProductField()
        time.sleep(3)
        self.elementClick(self._add_to_project)
        time.sleep(2)
        self.elementClick(self._click_sub_menu)
        time.sleep(2)
        accessory = self.getText(self._view_by_type_accessory_filter)
        accessory = accessory.split()
        accessory = accessory[0]
        text = "Accessory"
        self.verifyTextContains(actualText=accessory, expectedText=text)

    # TC 02 - Accessory added in bulk copy filter bucket

    def BulkCopyButton_VerifyAccessoryShowingTopOfList(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(5)
        self.elementClick(self._click_bulk_copy_button)
        time.sleep(2)
        list_text = "Bulk copy accessory"
        bulk_text = self.getText(self._bulk_copy_list)
        self.verifyTextContains(actualText=bulk_text, expectedText=list_text)
        self.add.clickAddAssignment() # Click on the assignment link
        self.RemoveAddedProduct() # Remove the product

    # TC 03 - Furniture added in View by type filter bucket

    def AddingFurnitureProduct_VerifyAddedInViewByType(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(2)
        self.add.addProduct()
        time.sleep(2)
        self.elementClick(self._click_furniture_filter)
        time.sleep(2)
        self.add.clickProductField()
        time.sleep(2)
        self.elementClick(self._add_to_project)
        time.sleep(2)
        self.elementClick(self._click_sub_menu)
        time.sleep(2)
        furniture = self.getText(self._view_by_type_furniture_filter)
        furniture = furniture.split()
        furniture = furniture[0]
        text = "Furniture"
        self.verifyTextContains(actualText=furniture, expectedText=text)

    # TC 04 - Furniture added in Bulk copy filter bucket

    def BulkCopyButton_VerifyFurnitureShowingTopOfList(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(4)
        self.elementClick(self._click_bulk_copy_button)
        time.sleep(2)
        list_text = "Bulk copy furniture"
        bulk_text = self.getText(self._bulk_copy_list)
        self.verifyTextContains(actualText=bulk_text, expectedText=list_text)
        self.add.clickAddAssignment()
        self.RemoveAddedProduct()

    # TC 05 - Office Furniture added in View by type filter bucket

    def AddingOfficeFurnitureProduct_VerifyAddedInViewByType(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(2)
        self.add.addProduct()
        time.sleep(2)
        self.elementClick(self._click_office_furniture_filter)
        time.sleep(2)
        self.add.clickProductField()
        time.sleep(2)
        self.elementClick(self._add_to_project)
        time.sleep(2)
        self.elementClick(self._click_sub_menu)
        time.sleep(2)
        office_furniture = self.getText(self._view_by_type_office_furniture_filter)
        office_furniture = office_furniture[:-4]
        text = "Office Furniture"
        self.verifyTextContains(actualText=office_furniture, expectedText=text)

    # TC 06 - Office Furniture added in Bulk Copy filter bucket

    def BulkCopyButton_VerifyOfficeFurnitureShowingTopOfList(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(5)
        self.elementClick(self._click_bulk_copy_button)
        time.sleep(2)
        list_text = "Bulk copy office furniture"
        bulk_text = self.getText(self._bulk_copy_list)
        self.verifyTextContains(actualText=bulk_text, expectedText=list_text)
        self.add.clickAddAssignment()
        self.RemoveAddedProduct()

    # TC 07 - Ops Asset added in View by type filter bucket

    def AddingOpsAssetProduct_VerifyAddedInViewByType(self):
        time.sleep(2)
        self.add = addRemoveProducts(self.driver)
        self.add.addProduct()
        time.sleep(2)
        self.elementClick(self._click_ops_asset_filter)
        time.sleep(2)
        self.add.clickProductField()
        time.sleep(2)
        self.elementClick(self._add_to_project)
        time.sleep(2)
        self.elementClick(self._click_sub_menu)
        time.sleep(2)
        ops_asset = self.getText(self._view_by_type_ops_asset_filter)
        ops_asset = ops_asset[:-4]
        text = "Ops Asset"
        self.verifyTextContains(actualText=ops_asset, expectedText=text)

    # TC 08 - Ops Asset added in bulk copy filter bucket

    def BulkCopyButton_VerifyOpsAssetFurnitureShowingTopOfList(self):
        self.add = addRemoveProducts(self.driver)
        time.sleep(4)
        self.elementClick(self._click_bulk_copy_button)
        time.sleep(2)
        list_text = "Bulk copy ops asset"
        bulk_text = self.getText(self._bulk_copy_list)
        self.verifyTextContains(actualText=bulk_text, expectedText=list_text)
        self.add.clickAddAssignment()
        self.RemoveAddedProduct()

