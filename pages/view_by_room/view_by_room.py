import time
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from pages.add_remove_product.add_remove_product_page import addRemoveProducts
from selenium.webdriver.common.action_chains import ActionChains


class ViewByRoom(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _all_rooms = "//span[contains(text(),'All rooms')]"
    _rooms_dropdown_click = "//div[contains(text(),'View rooms with products')]"
    _rooms_view_all_click = "//div[contains(text(),'View all rooms')]"
    _rooms_view_room_without_product_click = "//div[contains(text(),'View rooms without products')]"
    _thumbnail_icon = "//*[@class='svg-inline--fa fa-th fa-w-16 secondIcon']"
    _product_count = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div/div/div/p[contains(text(),'products')]"
    _all_room_text = "//h2[contains(text(),'All rooms')]"
    _success_toast_message = "//div[@class='Toastify__toast-body']"
    _assign_new_product_click = "//div[contains(text(),'Assign new products')]"
    _toast_message = ".Toastify__toast"
    _no_product = "//p[contains(text(),'There are no rooms with products. Please select a ')]"


    # test case

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view all 
    
    Verify : Count of room matches with total room.
    
    '''
    def AllRoomCount(self):
        time.sleep(20)
        self.ar = addRemoveProducts(self.driver)
        self.ar.clickProduct()
        time.sleep(2)
        self.webScroll(direction='down')
        time.sleep(2)
        self.waitForElement(self._all_rooms)
        self.elementClick(self._all_rooms)
        room_count = self.getText(self._all_rooms)
        room_count = room_count.split()
        room_count = room_count[2]
        room_count = room_count.replace("(", '')
        room_count = room_count.replace(")", '')
        self.log.info(room_count)
        time.sleep(2)
        self.elementClick(self._rooms_dropdown_click)
        time.sleep(2)
        self.elementClick(self._rooms_view_all_click)
        time.sleep(4)
        total_room = self.getText(self._product_count)
        total_room = total_room.split()
        total_room = total_room[0]
        self.log.info(total_room)
        self.verifyTextContains(actualText=total_room, expectedText=room_count)


    _select_checkbox = "//tr[1]//td[1]//div[1]//div[1]//input[1]"
    _apply_changes_button = "//span[contains(text(),'Apply Changes')]"
    _plus_button = "//tr[1]//div[1]//div[1]//button[2]"
    _add_edit_cancel_button = "//button/span[contains(text(),'Cancel')]"
    _close_button = "//div//button[@title = 'Close Dialog']"


    def ViewRoomWithoutProduct(self):
        time.sleep(2)
        self.elementClick(self._rooms_view_all_click)
        time.sleep(2)
        self.elementClick(self._rooms_view_room_without_product_click)

    def AddAssignment(self):
        time.sleep(2)
        self.ar = addRemoveProducts(self.driver)
        self.ar.clickAddAssignment()
        time.sleep(2)
        self.elementClick(self._assign_new_product_click)
        time.sleep(3)
        self.elementClick(self._select_checkbox)
        time.sleep(2)
        self.elementClick(self._plus_button)


    # TC 2 : Add product in room

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. Click apply changes button
    
    Verify : toast message should appear with success.
    
    '''

    def ProductAddInRoom(self):
        time.sleep(2)
        self.ViewRoomWithoutProduct()
        time.sleep(2)
        self.AddAssignment()
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(6)
        success_msg = 'Success'
        msg = self.getText(self._toast_message, locatorType='css')
        self.verifyTextContains(actualText=msg, expectedText=success_msg)


    # TC 03 Verify cancel button functionality

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. Click cancel button
    
    Verify count of room should not be changed.
    
    '''


    def ProductRoomCancelButton(self):
        time.sleep(2)
        count_of_product = self.getText(self._product_count)
        self.AddAssignment()
        time.sleep(2)
        self.elementClick(self._add_edit_cancel_button)
        time.sleep(2)
        productcount = self.getText(self._product_count)
        self.verifyTextContains(actualText=productcount, expectedText=count_of_product)

    # TC 04 Verify close button functionality

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. Click close button

    Verify count of room should not be changed.

    '''

    def ProductRoomCloseButton(self):
        time.sleep(2)
        count_of_product = self.getText(self._product_count)
        self.AddAssignment()
        time.sleep(2)
        self.elementClick(self._close_button)
        time.sleep(2)
        productcount = self.getText(self._product_count)
        self.verifyTextContains(actualText=productcount, expectedText=count_of_product)

    # TC 05 Search product using product name

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. Click on search box
    11. Enter product name

    Verify PRODUCT name enter should matches with the search result. 

    '''


    _search_filter_textbox = "//input[@placeholder='Search by product name, SKU']"
    _irrelevant_text = "//p[contains(text(),'Try another term or different spelling')]"
    _room_type_name_from_edit_address_window = "//tr[1]//td[2]//div[1]//a[1]//div[1]//div[1]"
    _sku = "//div[@class='sc-ifAKCX cZFrkc']//div[1]//span[@class='sc-dnqmqq QqDcF']"
    _detail_page_product_name = "//div[@id='root']/div/div[3]/div/div/div[2]/div[3]/div[2]/div/p[1]"

    def enterText(self, value):
        time.sleep(2)
        self.elementClick(self._search_filter_textbox)
        self.clearField(self._search_filter_textbox)
        time.sleep(2)
        self.sendKeys(value, self._search_filter_textbox)

    def sendKeyboardValues(self, value1):
        time.sleep(2)
        self.sendKeys(value1, self._search_filter_textbox)

    def SearchProductUsingProductName(self):
        time.sleep(2)
        self.AddAssignment()
        time.sleep(2)
        room_name = self.getText(self._room_type_name_from_edit_address_window)
        time.sleep(2)
        self.enterText(room_name)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        room_type_text = self.getText(self._room_type_name_from_edit_address_window)
        time.sleep(2)
        self.verifyTextContains(actualText=room_type_text, expectedText=room_name)

    # TC 06 Verify product name hyperlink and navigation

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. Click cancel button

    Verify : Clicking on product name should redirect user to product detail page. 
    '''

    def ClickProductName(self):
        time.sleep(2)
        self.AddAssignment()
        time.sleep(2)
        proname = self.getText(self._room_type_name_from_edit_address_window)
        window_before = self.driver.window_handles[0]
        self.elementClick(self._room_type_name_from_edit_address_window)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        detail_page_product_name = self.getText(self._detail_page_product_name)
        time.sleep(2)
        self.verifyTextContains(actualText=detail_page_product_name, expectedText=proname)

        # verify search using sku
        sku_number = self.getText(self._sku)
        self.driver.switch_to.window(window_before)
        time.sleep(2)
        self.enterText(sku_number)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        window_before = self.driver.window_handles[0]
        self.elementClick(self._room_type_name_from_edit_address_window)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        sku_number1 = self.getText(self._sku)
        time.sleep(2)
        self.verifyTextContains(actualText=sku_number1, expectedText=sku_number)
        self.driver.switch_to.window(window_before)

    # TC 07 Verify search message for in appropriate searching

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. click search button
    11. Enter irrelevant product name
    
    Verify appropriate message should be shown to the user.

    '''

    def IrrelevantProductNameSearch(self):
        time.sleep(2)
        room_name1 = 'testing12'
        self.enterText(room_name1)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        room_text = self.getText(self._irrelevant_text)
        time.sleep(2)
        self.log.info(room_text)
        self.verifyTextContains(actualText=room_text, expectedText='Try another term or different spelling')
        self.clearField(self._search_filter_textbox)
        self.sendKeyboardValues(Keys.ENTER)

    # TC 08 Verify message on edit existing window when no product available.

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. click search button
    11. Enter irrelevant product name
    12. Clear the search field
    13. Click on edit existing tab
    
    Verify user should able to see appropriate message.

    '''

    _no_product_assigned = "//p[contains(text(),'No products assigned')]"
    _edit_existing_tab = "//div[contains(text(),'Edit existing')]"

    def EmptyMessageOnEditExistingTab(self):
        time.sleep(2)
        self.elementClick(self._edit_existing_tab)
        time.sleep(2)
        none = self.getText(self._no_product_assigned)
        none_text = "No products assigned"
        self.verifyTextContains(actualText=none, expectedText=none_text)
        time.sleep(2)
        self.elementClick(self._close_button)

    # TC 09 Select view room with product from the dropdown

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. click search button
    11. Enter irrelevant product name
    12. Clear the search field
    13. Click on edit existing tab
    14. Click close icon
    15. Click on the dropdown
    16. Select view room with product

    Verify user should able to see assigned room.

    '''

    def SelectViewRoomWithProduct(self):
        time.sleep(2)
        self.elementClick(self._rooms_view_room_without_product_click)
        time.sleep(2)
        self.elementClick(self._rooms_dropdown_click)


    _total_price = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[1]//strong[contains(., '$')]"
    _click_assign = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[1]//a[contains(., 'Assign')]"
    _p_quantity = '''//*[@id="root"]/div/div[3]/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr/td[3]/div'''
    _minus_button = "//tr[1]//div[1]//div[1]//button[1]"

    # TC 10 Verify user should able to decrease the quantity of product using plus button

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. click search button
    11. Enter irrelevant product name
    12. Clear the search field
    13. Click on edit existing tab
    14. Click close icon
    15. Click on the dropdown
    16. Select view room with product
    17. Click add assign link
    18. Click plus button
    19. Click apply changes button


    Verify product quantity should increase by 1

    '''

    def quantityIncrease(self):
        time.sleep(2)
        click_product_quantity = self.getText(self._p_quantity)
        time.sleep(1)
        self.elementClick(self._click_assign)
        time.sleep(2)
        self.elementClick(self._plus_button)
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(10)
        updated_product_quantity = self.getText(self._p_quantity)
        time.sleep(2)
        click_product_quantity = int(click_product_quantity)
        click_product_quantity = str(int(click_product_quantity) + int(1))
        time.sleep(2)
        self.verifyTextContains(actualText=click_product_quantity, expectedText=updated_product_quantity)


    # TC 11 Verify user should able to decrease the quantity of product using minus button

    '''
    1. Login to web-app
    2. Click on any project
    3. Click view all room
    4. Click view room with product drop down
    5. Select view room without product detail
    6. Click add assign link
    7. Click assign to product
    8. Select first checkbox
    9. Increase quantity by 1 using plus icon
    10. click search button
    11. Enter irrelevant product name
    12. Clear the search field
    13. Click on edit existing tab
    14. Click close icon
    15. Click on the dropdown
    16. Select view room with product
    17. Click add assign link
    18. Click minus button
    19. Click apply changes button


    Verify product quantity should decrease by 1

    '''

    def quantityDecrease(self):
        time.sleep(2)
        click_product_quantity1 = self.getText(self._p_quantity)
        click_product_quantity1 = click_product_quantity1.replace(',', '')
        time.sleep(1)
        self.elementClick(self._click_assign)
        time.sleep(2)
        self.elementClick(self._minus_button)
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(10)
        updated_product_quantity = self.getText(self._p_quantity)
        time.sleep(2)
        click_product_quantity1 = str(int(click_product_quantity1) - int(1))
        time.sleep(2)
        self.verifyTextContains(actualText=updated_product_quantity, expectedText=click_product_quantity1)

    # TC 12 - Failure Msg entering long irrelevant data

    '''

    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with unassigned products or products assigned to rooms

    Steps

    1) Click on the "+ Assign/edit rooms" button
    2) Update the quantity with irrelevant data like "1647657545455456"
    3) Click on 'Apply Changes' button

    Expected Result
    Appropriate toast message i.e. "Oh no! There was a problem with that assignment. Please try again" should be display.

    '''

    _enter_quantity_in_qty_checkbox = "//tr[1]//td[2]//div[1]//div[1]//div[1]//div[1]//input[1]"

    def enterQuantity(self, value):
        self.clearField(self._enter_quantity_in_qty_checkbox)
        self.sendKeys(value, self._enter_quantity_in_qty_checkbox)

    def enterIrrelevantDataInQuantity(self):
        time.sleep(2)
        self.elementClick(self._click_assign)
        time.sleep(3)
        self.enterQuantity('22222222222222224')
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(2)
        toast_message = self.getText(self._toast_message, locatorType='css')
        failed_message = "Oh no! There was a problem with that assignment. Please try again."
        self.verifyTextContains(actualText=toast_message, expectedText=failed_message)

    # 13 TC - 'Edit existing' Tab - 'Apply Changes' button Functionality after removing the room

    '''

    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps
    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Add/edit room" button
    5) Make changes in the existing room assignments e.g delete a room
    6) Click on the 'Apply Changes' button

    if rooms are multiple then verify second room shifted to first room
    if room is only one then verify add assignment text on product detail page. 

    Expected Result
    Modal box should get closed
    Relevant toast message should be displayed
    User should get redirected to the project purchase list
    Changes made in the room assignment should be reflected for the product on the project purchase list table


    '''

    _second_row_available = "//tr[2]//td[4]//div[1]//div[2]"
    _first_row = "//tr[1]//td[4]//div[1]//div[2]"
    element1 = "//td[4]/div/div[2]"

    def deleteRoomChangesApply(self):
        time.sleep(2)
        self.elementClick(self._click_assign)
        time.sleep(2)
        if self.isElementPresent(self._second_row_available) == True:
            text_second_room = self.getText(self._second_row_available)
            element_to_hover_over = self.getElement(self.element1)
            self.log.info('element found')
            hoverover = ActionChains(self.driver).move_to_element(element_to_hover_over).click().perform()
            time.sleep(2)
            first_row = self.getText(self._first_row)
            self.verifyTextContains(actualText=first_row, expectedText=text_second_room)
        else:
            element_to_hover_over = self.getElement(self.element1)
            self.log.info('element found')
            hoverover = ActionChains(self.driver).move_to_element(element_to_hover_over).click().perform()
            time.sleep(2)
            actual_text = self.getText(self._no_product_assigned)
            time.sleep(2)
            text_to_verify = "No products assigned"
            self.verifyTextContains(actualText=actual_text, expectedText=text_to_verify)


    # TC 14 Verify clicking on cancel button redirect user to product detail screen

    '''
    1. Delete the product
    2. Click cancel button

    Verify cancel button work and user redirect back to product detail screen.
    
    '''

    _add_more_product = "//span[contains(text(),'Add more products')]"

    def EditExistingCancelButton(self):
        time.sleep(2)
        self.elementClick(self._add_edit_cancel_button)
        time.sleep(2)
        check_button = self.getText(self._add_more_product)
        time.sleep(2)
        button_text = "Add more products"
        self.verifyTextContains(actualText=check_button, expectedText=button_text)
