import time
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class addRemoveProducts(SeleniumDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:
    _first_product = "//p[contains(text(),'12 Calle de Prim - P1')]"
    _add_more_product = "//span[contains(text(),'Add more products')]"
    _click_product = '''//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div'''
    _product_detail_name = "//div[@id='root']/div/div[3]/div/div/div[2]/div[3]/div[2]/div/p[1]"
    _add_to_project = "//span[contains(text(),'Add to project')]"
    _click_sub_menu = "//span[3][contains(text(),'12 Calle de Prim - P1')]"

    _product_name1 = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[3]/div/div/div[2]/p[1]"
    _add_assignment = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[2]//a[contains(., 'Assign')]"
    _remove_product = "remove product from project"
    _remove_popup_button = "//button/span[contains(text(),'Remove')]"
    _toast_message = ".Toastify__toast"


    _scroll_to_element = "//div[4]//div[1]//div[1]//div[2]//div[1]//div[3]"
    _view_by_type_added_product = "//div[@id='project-page-filter-menu-container']/div[5]/div/span"
    _product_type = "//div[@class='rah-static rah-static--height-auto']//div[5]//span[2]"


    _remove_product_text = "//p[contains(.,'Are you sure you want to remove this product from your project? Removing this product would also remove all current room assignments.')]"
    _cancel_button_modal_box = "//div[@id='root']/div[3]/div/div/div[3]/div/button/span[contains(text(),'Cancel')]"
    _modal_text_assignment_title = "//div/span[contains(text(),'Assign/edit rooms')]"

    _minus_button = "//div[@id='root']//tr[1]//td[5]//div[1]//div[1]//button[1]"
    _plus_button = "//div[@id='root']//tr[1]//td[5]//div[1]//div[1]//button[2]"

    _product_quantity = "//div[2]/div[2]/table[2]/tbody[1]/tr[1]/td[2]/div[1]"
    _close_button = "//div//button[@title = 'Close Dialog']"

    _add_edit_cancel_button = "//button/span[contains(text(),'Cancel')]"

    # no assignment text
    #_verify_view_unassigned_text = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[2]/div/p"
    _verify_view_unassigned_text = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[2]/div/p"

    def clickProduct(self):
        self.waitForElement(self._first_product)
        self.elementClick(self._first_product)

    def addProduct(self):
        self.waitForElement(self._add_more_product)
        self.elementClick(self._add_more_product)

    def clickProductField(self):
        self.waitForElement(self._click_product)
        self.elementClick(self._click_product)

    def clicksubMenu(self):
        self.elementClick(self._click_sub_menu)

    def clickAddAssignment(self):
        self.elementClick(self._add_assignment)

    def clickRemoveProduct(self):
        self.elementClick(self._remove_product, locatorType='link')

    def clickRemoveButton(self):
        self.elementClick(self._remove_popup_button)


    # adding a product
    def add(self):
        time.sleep(45)
        self.clickProduct()
        time.sleep(2)
        self.addProduct()
        time.sleep(2)
        self.clickProductField()
        time.sleep(2)
        button = self.isElementPresent(self._add_to_project)
        if button == True:
            self.log.info('hi this is true case')
            product_name = self.getText(self._product_detail_name)
            time.sleep(2)
            product_type = self.getText(self._product_type)
            self.elementClick(self._add_to_project)
        else:
            self.log.info('hi this is a false case')
            scroll = self.driver.execute_script("window.scrollBy(0, -250);")
            time.sleep(2)
            self.elementClick(self._scroll_to_element)
            time.sleep(2)
            product_name = self.getText(self._product_detail_name)
            time.sleep(2)
            product_type = self.getText(self._product_type)
            self.elementClick(self._add_to_project)

        self.clicksubMenu()
        time.sleep(2)
        product_name1 = self.getText(self._product_name1)
        time.sleep(2)
        self.waitForElement(self._view_by_type_added_product)
        view_by_type = self.getText(self._view_by_type_added_product)
        view_by_type = view_by_type.split()
        view_by_type = view_by_type[0]
        #self.verifyTextContains(actualText=product_type, expectedText=view_by_type)


    # 05 - 06  TC - 'Edit existing' Tab - Search Functionality

    '''
    
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Add/edit room" button
    5) Click on the Search panel 
    6) Type any relevant text
    7) Hit enter key from the keyboard

    Expected Result
    Relevant result results should be displayed when a search is made

    8) Clear the search by keyboard's backspace
    9) Hit enter key from the keyboard

    Expected Result
    Search result should get reset and default list should be displayed
    Steps
    10) Search for any irrelevant room

    Expected Result
    appropriate message should be displayed
    
    '''

    _search_filter_textbox = "//input[@placeholder='Filter by room number, type...']"
    _irrelevant_text = "//p[contains(text(),'testing')]"
    _room_type_name_from_edit_address_window = "//tr//td[3]"


    def enterText(self, value):
        time.sleep(2)
        self.elementClick(self._search_filter_textbox)
        self.clearField(self._search_filter_textbox)
        time.sleep(2)
        self.sendKeys(value, self._search_filter_textbox)

    def sendKeyboardValues(self, value1):
        time.sleep(2)
        self.sendKeys(value1, self._search_filter_textbox)

    def searchRelevantKeyword(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        room_name = self.getText(self._room_type_name_from_edit_address_window)
        self.enterText(room_name)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        room_type_text = self.getText(self._room_type_name_from_edit_address_window)
        time.sleep(2)
        self.verifyTextContains(actualText=room_type_text, expectedText=room_name)

    def searchIrrelevantKeyword(self):
        time.sleep(2)
        room_name1 = 'testing'
        self.enterText(room_name1)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        room_type_text = self.getText(self._irrelevant_text)
        time.sleep(2)
        self.verifyTextContains(actualText=room_type_text, expectedText='No results for "testing"')
        self.clearField(self._search_filter_textbox)
        self.sendKeyboardValues(Keys.ENTER)

    # 07-08 TC - 'Floor' drop-down filter Functionality

    '''
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Add/edit room" button
    5) Click on the 'Select a floor' drop-down filter button

    Expected Result
    Floor drop-down list should get invoked
    All the floors should be listed under the drop-down list
    Steps
    6) Click on the any of the floor from the list

    Expected Result
    Room list should display the results as per the selected floor filter
    When no result found, appropriate message should be displayed in the room list
    
    '''

    _select_a_floor = "//div[@id='root']/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div/div[1]"
    floor = '''//*[@id="react-select-3-input"]'''
    #_select_first_floor = "//body/div[2]/div/div/div[3]"  --- qa
    _select_first_floor = "//body/div[4]/div/div/div[3]"  #beta
    #_select_second_floor = "//body/div[2]/div/div/div[4]"
    _select_second_floor = "//body/div[4]/div/div/div[4]"
    _floor_value = "//td//div[contains(text(),'1st Floor')]"
    _without_floor_data = "//div[@id='root']/div[2]/div/div/div[2]/div/div[3]/p[1]"

    def floorSelection(self):
        time.sleep(2)
        self.elementClick(self._select_a_floor)
        time.sleep(2)
        text = '1st Floor'
        self.elementClick(self._select_first_floor)
        time.sleep(2)
        floor_value = self.getText(self._floor_value)
        self.verifyTextContains(actualText=floor_value, expectedText=text)

    def floorWithoutDateSelection(self):
        time.sleep(2)
        text = 'No results for "2nd Floor"'
        self.elementClick(self._select_a_floor)
        time.sleep(2)
        self.elementClick(self._select_second_floor)
        time.sleep(2)
        without_data = self.getText(self._without_floor_data)
        time.sleep(2)
        self.verifyTextContains(actualText=without_data, expectedText=text)


    # 09 TC - 'Edit existing' Tab - 'Cancel' button Functionality

    '''
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps
    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Assign/edit rooms"
    5) Increase or decrease the qty for existing product 
    6) Delete a room assignment 
    7) Click on the Cancel button from bottom left right corner of the modal box

    Expected Result
    Modal box should get closed
    User should get redirected to the Project purchase list
    No changes should be reflected to the product's room assignment table
    
    '''

    def addEditButtonCancelFunctionality(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.elementClick(self._add_edit_cancel_button)
        time.sleep(2)
        button_text = "Add more products"
        check_button = self.getText(self._add_more_product)
        time.sleep(2)
        self.verifyTextContains(actualText=check_button, expectedText=button_text)


    # 10 - 11 TC - 'Edit existing' Tab - Qty increase/decrease Functionality
    '''
    
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Add/edit room" button
    5) Click on the '+' button of room assignment under Qty column

    Expected Result
    Product's quantity should get increased by 1 on clicking the + button

    6) Click on the '-' button of room assignment under Qty column

    Expected Result
    Product's quantity should get decreased by 1 on clicking the '-' button
    
    '''

    def quantityIncrease(self):
        time.sleep(2)
        click_product_quantity = self.getText(self._product_quantity)
        click_product_quantity = click_product_quantity.replace(',', '')
        time.sleep(1)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.elementClick(self._plus_button)
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(2)
        updated_product_quantity = self.getText(self._product_quantity)
        time.sleep(2)
        click_product_quantity = int(click_product_quantity)
        click_product_quantity = str(int(click_product_quantity) + int(1))
        time.sleep(2)
        self.verifyTextContains(actualText=click_product_quantity, expectedText=updated_product_quantity)

    def quantityDecrease(self):
        time.sleep(2)
        click_product_quantity1 = self.getText(self._product_quantity)
        click_product_quantity1 = click_product_quantity1.replace(',', '')
        time.sleep(1)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.elementClick(self._minus_button)
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(2)
        updated_product_quantity = self.getText(self._product_quantity)
        time.sleep(2)
        click_product_quantity1 = str(int(click_product_quantity1) - int(1))
        time.sleep(2)
        self.verifyTextContains(actualText=updated_product_quantity, expectedText=click_product_quantity1)


    # 12- 01 TC - Failure Msg entering irrelevant data - Room Assignments- View by typeest

    '''
    
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with unassigned products or products assigned to rooms

    Steps
    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Assign/edit rooms" button
    5) Click on the 'Assign to new rooms' tab
    6) Update the quantity with irrelevant data like "1647657545455456"
    7) Click on 'Apply Changes' button

    Expected Result
    Appropriate toast message i.e. "Failed to assign product to room(s)." should be displayed
    
    
    '''

    _enter_quantity_in_qty_checkbox = "//input[@placeholder='2']"

    def enterQuantity(self, value):
        self.elementClick(self._enter_quantity_in_qty_checkbox)
        self.sendKeys(value, self._enter_quantity_in_qty_checkbox)

    def enterIrrelevantDataInQuantity(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.enterQuantity('22222222222222224')
        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(2)
        toast_message = self.getText(self._toast_message, locatorType='css')
        failed_message = "Failed to assign product to room(s)."
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


    _second_row_available = "//tr[2]//td[3]//div[1]//div[1]//div[1]"
    _first_row = "//tr[2]//td[3]//div[1]//div[1]//div[1]"

    def deleteRoomChangesApply(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        if self.isElementPresent(self._second_row_available)== True:
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
            actual_text = self.getText(self.message_after_delete)
            time.sleep(2)
            text_to_verify = "This product is not yet assigned to any rooms"
            self.verifyTextContains(actualText=actual_text, expectedText=text_to_verify)


    # 14 TC - 'Edit existing' Tab - Bin button Functionality

        '''

        Preconditions
        1) User should be logged in to the app
        2) User should have some Projects with products assigned to rooms

        Steps
        1) Login to the app
        2) Click on any project from the Dashboard
        3) Locate a product assigned to rooms
        4) Click on the "+ Add/edit room" button
        5) Hover the mouse at the extreme right side at any of the room row in the list
        6) Click on the bin button

        Expected Result
        The room should get deleted from the list on clicking

        '''

    element1 = "//div[@id='root']/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[5]/div/div[2]"
    message_after_delete = "//p[contains(text(),'This product is not yet assigned to any rooms')]"


    def binButton(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        for i in range(20):
            if self.isElementDisplayed(self.element1) == True:
                element_to_hover_over = self.getElement(self.element1)
                self.log.info('element found')
                hoverover = ActionChains(self.driver).move_to_element(element_to_hover_over).click().perform()
                self.log.info('element clicked')
            else:
                break
        time.sleep(5)
        text_after_delete = "This product is not yet assigned to any rooms"
        text_bin = self.getText(self.message_after_delete)
        self.verifyTextContains(actualText=text_bin, expectedText=text_after_delete)

    # 15 TC - 'Edit existing' Tab - Close(X) button Functionality

        '''

        Preconditions
        1) User should be logged in to the app
        2) User should have some Projects with products assigned to rooms

        Steps
        1) Login to the app
        2) Click on any project from the Dashboard
        3) Locate a product assigned to rooms
        4) Click on the "+ Assign/edit rooms"
        5) Increase or decrease the qty for existing product 
        6) Delete a room assignment 
        7) Click on the Close (X) button from top right corner of the modal box

        Expected Result
        Modal box should get closed
        User should get redirected to the Project purchase list
        No changes should be reflected to the product's room assignment table
        Note: Please verify the Close (X) button functionality throughout the process

        '''

    def closeButton(self):
        time.sleep(3)
        self.elementClick(self._close_button)


    # 16 TC - Link to the product details functionality

    '''
    
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with unassigned products or products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to a few rooms (view by type)
    4) Click on the "+ Assign/edit rooms" button
    5) Hover the mouse over the product name located next to the modal box header text

    Expected Result
    Hovering over the product name should underline the item and should display the new tab icon

    Steps
    6) Click on the Product name hyperlink

    Expected Result
    User should get redirected to that product detail page of that product in a new tab
    
    '''

    _product_detail_link_add_assignment_modal_box = "//div[@id='root']/div[2]/div/div/div/div/div/span[2]/a"
    _detail_page_product_name = "//div[@id='root']/div/div[3]/div/div/div[2]/div[3]/div[2]/div/p[1]"

    def productLinkInEditBox(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        name_product = self.getText(self._product_detail_link_add_assignment_modal_box)
        window_before = self.driver.window_handles[0]
        self.elementClick(self._product_detail_link_add_assignment_modal_box)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.isElementDisplayed(self._detail_page_product_name)
        detail_page_product_name = self.getText(self._detail_page_product_name)
        time.sleep(2)
        self.verifyTextContains(actualText=detail_page_product_name, expectedText=name_product)
        self.driver.switch_to.window(window_before)


    # 17-19 Tc - # Removing a product from product detail page

    '''

    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate a product assigned to rooms
    4) Click on the "+ Assign/edit rooms"
    5) Click on the hyperlink text "remove product from project."

    Expected Result
    "Remove product?" confirmation modal box should get invoked
    Modal box should contain the text i.e. "Are you sure you want to remove this product from your project? Removing this product would also remove all current room assignments."
    Cancel & Remove button should be displayed at the bottom of the box
    Current room assignment details (e.g Qty & Room) should appear correctly
    'Apply Changes' button should be enabled

    6) Click on the "Remove" button

    Expected Result
    The product should get removed from the purchase list with its current room assignments.
    User should get redirected to the purchase list


    '''

    def removeProductText(self):
        time.sleep(5)
        self.clickRemoveProduct()
        remove_text = self.getText(self._remove_product_text)
        remove_text1 = "Are you sure you want to remove this product from your project? Removing this product would also remove all current room assignments."
        self.verifyTextContains(actualText=remove_text, expectedText=remove_text1)

    def cancelButton(self):
        time.sleep(2)
        self.elementClick(self._cancel_button_modal_box)
        time.sleep(2)
        modal_text = "Assign/edit rooms"
        modal_text_title = self.getText(self._modal_text_assignment_title)
        time.sleep(2)
        self.verifyTextContains(actualText=modal_text_title, expectedText=modal_text)

    def remove(self):
        time.sleep(2)
        self.clickRemoveProduct()
        time.sleep(2)
        self.clickRemoveButton()
        time.sleep(2)

    ###############################################################################################

    _product_count = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div/div/div/p[contains(text(),'products')]"
    _home_submenu = "//span[contains(.,'Home')]"
    _product_view_count = "//span[contains(text(),'All products')]"


    # Product count on product detail page after adding a product
    def productAddedViewByType(self):
        count = self.getText(self._product_count)
        count = count.split()
        count = count[0]
        view_by_type = self.getText(self._product_view_count)
        view_by_type = view_by_type.replace("(", '')
        view_by_type = view_by_type.replace(")", '')
        view_by_type = view_by_type.split()
        view_by_type = view_by_type[2]
        self.verifyTextContains(actualText=count, expectedText=view_by_type)


    '''def RoomAssignments(self):
        count = self.getText(self._product_count)
        count = count.split()
        count = count[4:]
        if self.test == count:
            return True
        else:
            return False'''


    #####################################################################################################

    _assign_new_room = "//div[contains(text(),'Assign to new rooms')]"
    _product_price = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div/div/div[2]/div/span"
    _enter_quantity = "//input[@placeholder='2']"
    _verify_added_list = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]"
    _apply_changes_button = "//span[contains(text(),'Apply Changes')]"
    _subtotal = "//div[@id='project-page-header-container']//div[3]//div[4]//p[2]"
    _add_new_room_plus_button = "//tr[1]//td[6]//div[1]//div[1]//button[2]"
    _add_new_room_minus_button = "//tr[1]//td[6]//div[1]//div[1]//button[1]"
    _add_new_room_room_type_name = "//tr[1]//td[4]"
    temp_var = "//input[@placeholder='2']"

    def clickAssignNewRoom(self):
        self.elementClick(self._assign_new_room)

    # assign rooms and unit
    def addRoomAssignment(self):
        time.sleep(4)
        product_price = self.getText(self._product_price)
        product_price = product_price.replace('$', '')
        product_price = product_price.replace(',', '')
        subtotal = self.getText(self._subtotal)
        subtotal = subtotal.replace('$', '')
        subtotal = subtotal.replace(',', '')
        time.sleep(2)
        self.clickAddAssignment()
        time.sleep(2)
        self.clickAssignNewRoom()
        time.sleep(2)
        a = "//tr"
        b = "//td[1]//div[1]//input[1]"
        button = "//tr"
        button1 = "//div[1]//div[1]//button[2]"
        for i in range(1, 20):
            x = [i]
            checkbox_xpath = a + str(x) + b
            click_new_room_plus = button + str(x) + button1
            time.sleep(2)
            if self.getElement(checkbox_xpath).is_selected() == True:
                continue
            else:
                self.log.info('not enabled')
                self.elementClick(checkbox_xpath)
                self.elementClick(click_new_room_plus)
                break

        time.sleep(2)
        self.elementClick(self._apply_changes_button)
        time.sleep(3)
        value = float(2)
        subtotal1 = self.getText(self._subtotal)
        time.sleep(2)
        if subtotal1 != '-':
            self.log.info('not equal to -')
            calculate = str(float(product_price) * float(value))
            calculate = str(float(calculate) + float(subtotal))
            time.sleep(2)
            subtotal = self.getText(self._subtotal)
            subtotal = subtotal.replace('$', '')
            subtotal = subtotal.replace(',', '')
            self.verifyTextContains(actualText=calculate, expectedText=subtotal)
        '''else:
            self.log.info('equal to -')
            time.sleep(4)
            subtotal = self.getText(self._subtotal)
            subtotal = subtotal.replace('$', '')
            subtotal = subtotal.replace(',', '')
            subtotal = subtotal[:-1]
            self.verifyTextContains(actualText=calculate, expectedText=subtotal)'''

    # 'Assign to new rooms' Tab - Search Functionality

    '''
    
    Steps
    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate an unassigned product 
    4) Click on the "+ Assign rooms" button
    5) Click on the 'Assign to new rooms' tab
    6) Click on the Search panel 
    7) Type any relevant text
    8) Hit enter key from the keyboard

    Expected Result
    Relevant result results should be displayed when a search is made
    2
    9) Clear the search by keyboard's backspace
    10) Hit enter key from the keyboard

    Expected Result
    Search result should get reset and default list should be displayed
    Steps
    11) Search for any irrelevant room

    Expected Result
    Appropriate message should be displayed
    
    '''

    def assign_new_room(self):
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.elementClick(self._assign_new_room)
        time.sleep(2)
        room_name = self.getText(self._room_type_name_from_edit_address_window)
        self.enterText(room_name)
        self.sendKeyboardValues(Keys.ENTER)
        time.sleep(2)
        room_type_text = self.getText(self._room_type_name_from_edit_address_window)
        time.sleep(2)
        self.verifyTextContains(actualText=room_type_text, expectedText=room_name)

    def AssignToNewRoom_searchFunctionality(self):
        if self.isElementPresent(self._add_assignment) == True:
            self.assign_new_room()
        else:
            self.add()
            self.assign_new_room()

    def AssignToNewRoom_IrreleavantSearchFunctionality(self):
        self.searchIrrelevantKeyword()



    # 'Assign to new rooms' Tab - 'Floor' drop-down filter Functionality


    '''
    Preconditions
    1) User should be logged in to the app
    2) User should have some Projects with unassigned products or products assigned to rooms

    Steps

    1) Login to the app
    2) Click on any project from the Dashboard
    3) Locate an unassigned product 
    4) Click on the "+ Assign rooms" button
    5) Click on the 'Assign to new rooms' tab
    6) Click on the 'Select a floor' drop-down filter button

    Expected Result
    Floor drop-down list should get invoked
    All the available floors should be listed under the drop-down list
    Steps
    7) Click on the any of the floor from the list

    Expected Result
    Room list should display the results as per the selected floor filter
    When no result found, appropriate message should be displayed in the room list
    
    '''

    def AssignToNewRoom_FloorFilterDropDown(self):
        time.sleep(2)
        self.floorSelection()
        self.elementClick(self._add_edit_cancel_button)


    # verify product dropdown filter functionality on product detail screen


    _click_product_dropdown = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div"
    _click_view_unassigned = "//div[2]/div/div/div/div[2]/div/div[2]"
    _click_view_assigned = "//div[2]/div/div/div/div[2]/div/div[3]"

    _verify_view_assigned_text = "//div[@id='root']//div[2]/div[2]//h3[contains(.,'Room')]"


    def ProductDetailScreen_ProductDropdownUnassigned(self):
        self.elementClick(self._add_edit_cancel_button)
        time.sleep(2)
        self.elementClick(self._click_product_dropdown)
        time.sleep(2)
        self.elementClick(self._click_view_unassigned)
        time.sleep(2)
        verify_text = self.getText(self._verify_view_unassigned_text)
        verify_text = verify_text[:47]
        text = 'There are no room assignments for this product.'
        self.verifyTextContains(actualText=verify_text, expectedText=text)

    def ProductDetailScreen_ProductDropdownAssigned(self):
        time.sleep(2)
        self.elementClick(self._click_product_dropdown)
        time.sleep(2)
        self.elementClick(self._click_view_assigned)
        time.sleep(2)
        verify_text = self.getText(self._verify_view_assigned_text)
        text = 'Room'
        self.verifyTextContains(actualText=verify_text, expectedText=text)































