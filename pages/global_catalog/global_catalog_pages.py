import time
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver


class GlobalCatalog(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    phoenix_text = "//p[contains(text(),'Phoenix global catalog')]"
    _click_first_img = "//div[@class='image-grid']//div[@class='left-top']//img"
    _check_global_catalog_redirection = "//span[contains(.,'Global catalog')]"

    def catalogPage(self):
        time.sleep(15)
        text = self.getText(self.phoenix_text)
        actual_text = 'Phoenix global catalog'
        self.verifyTextContains(actualText=actual_text, expectedText=text)
        self.waitForElement(self._click_first_img)
        self.elementClick(self._click_first_img)
        time.sleep(2)
        text_re = self.getText(self._check_global_catalog_redirection)
        time.sleep(1)
        self.verifyTextContains(actualText=text_re, expectedText="Global catalog")


    # Test case 2 - GC- Indicate logged in user

    _user_profile_icon = "//img[contains(@src,'https://lh4.googleusercontent.com/-l0Nse9g06Lk/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3reoOmkz5csX7CYFMarjSm6XD9HFwQ/photo.jpg')]"

    def userProfilePicture(self):
        self.waitForElement(self._user_profile_icon)
        result = self.isElementPresent(self._user_profile_icon)
        return result


    # Test case 3 - GC- Filters Panel

    _filter = "//h2[contains(text(),'Filters')]"
    _availability = "//h4[contains(text(),'Availability')]"
    _collection = "//h4[contains(text(),'Collection')]"
    _region = "//h4[contains(text(),'Region')]"
    _type = "//h4[contains(text(),'Type')]"
    _sub_type = "//h4[contains(text(),'Sub type')]"
    _manufacture = "//h4[contains(text(),'Manufacturer')]"
    _vendor = "//h4[contains(text(),'Vendor')]"
    _material_type = "//h4[contains(text(),'Material type')]"

    def filterLabel(self):
        actual = 'Filters'
        filter_label = self.getText(self._filter)
        self.verifyTextContains(actualText=filter_label, expectedText=actual)

    def availabilityLabel(self):
        actual = 'Availability'
        label = self.getText(self._availability)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def collectionFilter(self):
        actual = 'Collection'
        label = self.getText(self._collection)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def regionFilter(self):
        actual = 'Region'
        label = self.getText(self._region)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def typeFilter(self):
        actual = 'Type'
        label = self.getText(self._type)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def subTypeFilter(self):
        actual = 'Sub type'
        label = self.getText(self._sub_type)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def manufactureFilter(self):
        actual = 'Manufacturer'
        label = self.getText(self._manufacture)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def vendorFilter(self):
        actual = 'Vendor'
        label = self.getText(self._vendor)
        self.verifyTextContains(actualText=label, expectedText=actual)

    def materialFilter(self):
        actual = 'Material type'
        label = self.getText(self._material_type)
        self.verifyTextContains(actualText=label, expectedText=actual)

    _region_position = "//h4[contains(text(),'Region')]"
    _see_more = "//div[4]//span[contains(text(),'See more')]"
    #old = "//div[4]//ul[1]//li[7]//span[1]"
    _see_less = "//span[contains(text(),'See Less')]"


    def checkSeeMorelink(self):
        time.sleep(2)
        if self.isElementPresent(self._region_position) == True:
            self.elementClick(self._see_more)
            time.sleep(2)
            see_less = self.getText(self._see_less)
            text = "See Less"
            self.verifyTextContains(actualText=see_less, expectedText=text)
            time.sleep(2)
            self.elementClick(self._see_less)
            time.sleep(2)
            see_more = self.getText(self._see_more)
            text = "See more"
            self.verifyTextContains(actualText=see_more, expectedText=text)

    _filter_click = "//label[contains(.,'Bulk 1.0')]"
    _clear_filter = "//p[contains(text(),'Clear filters')]"


    def applyFilter(self):
        time.sleep(2)
        self.webScroll(direction="up")
        self.waitForElement(self._filter_click)
        self.elementClick(self._filter_click)
        time.sleep(2)
        self.waitForElement(self._clear_filter)
        clear_filter = self.getText(self._clear_filter)
        self.verifyTextContains(actualText=clear_filter, expectedText='Clear filters')
        time.sleep(2)


    # Check filter values after applying the filters.

    # Applied filter on listing screen
    _type_select = "//div[5]//ul[1]//li[1]//div[1]"
    _sub_type_click = "//div[6]//ul[1]//li[1]//div[1]"
    _manufacture_click = "//div[7]//ul[1]//li[1]//div[1]"

    # detail page filter value verification
    _manufacture_value = "//div[@class='rah-static rah-static--height-auto']//div[2]//span[2]"
    _type_value = "//div[@class='rah-static rah-static--height-auto']//div[5]//span[2]"
    _subtype_value = "//div[@class='rah-static rah-static--height-auto']//div[6]//span[2]"

    # click on first cell after applying the filter

    _first_cell = '''//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div'''


    def clickFirstCell(self):
        self.waitForElement(self._first_cell)
        self.elementClick(self._first_cell)

    def verifyAppliedFilterDetailPage(self):
        time.sleep(5)
        self.elementClick(self._clear_filter)
        time.sleep(3)
        self.elementClick(self._filter_click)
        time.sleep(3)
        collection = self.getText(self._filter_click)
        self.elementClick(self._type_select)
        time.sleep(2)
        typefilter = self.getText(self._type_select)
        time.sleep(3)
        self.elementClick(self._sub_type_click)
        sub_type = self.getText(self._sub_type_click)
        time.sleep(3)
        self.elementClick(self._manufacture_click)
        manufacture = self.getText(self._manufacture_click)
        time.sleep(3)
        self.clickFirstCell()
        time.sleep(3)
        subtype_detail_value = self.getText(self._subtype_value)
        type_detail_value = self.getText(self._type_value)
        manufacture_detail_value = self.getText(self._manufacture_value)
        self.verifyTextContains(actualText=typefilter, expectedText=type_detail_value)
        self.verifyTextContains(actualText=sub_type, expectedText=subtype_detail_value)
        self.verifyTextContains(actualText=manufacture, expectedText=manufacture_detail_value)

    # GC- Search Box

    '''

       Steps
       1) Login to the web app with valid email and proceed to the Dashboard
       2) Scroll down to 'Phoenix global catalog' and click on the 'browse Global Catalog' picture 
       3) Locate the search box

       Expected Result
       Page should contain the Search box at the top of the screen next to the Filters panel
       - Search box field should contain placeholder text 'Filter by product name, SKU'
       - User should be able to search items by Product name, SKU name ( Fuzzy match, Elastic Search should function accordingly)

    '''

    _search_box = '''//input[@placeholder='Filter by product name, SKU']'''
    _product_name = '''//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div[2]/p[1]'''
    _second_product_name = "//body//div[@class='sc-bnXvFD irlgiv']/div[2]//p[@class='sc-krvtoX cIPoqq']"
    _submenu_click = "//span[contains(.,'Global catalog')]"

    def searchBox(self):
        time.sleep(2)
        self.elementClick(self._submenu_click)
        time.sleep(2)
        self.waitForElement(self._clear_filter)
        self.elementClick(self._clear_filter)
        time.sleep(5)
        product_name = self.getText(self._product_name)
        time.sleep(2)
        self.elementClick(self._search_box)
        time.sleep(4)
        self.EnterProductName(str(product_name))
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(2)
        productName = self.getText(self._product_name)
        self.verifyTextContains(actualText=product_name, expectedText=productName)
        '''second_product = self.getText(self._second_product_name)
        time.sleep(2)
        second_product = second_product.split()
        for i in second_product:
            if i == 'Rustic':
                return True
            elif i == 'copper':
                return True
            elif i == 'wallet':
                return True
            else:
                return False'''

    def EnterProductName(self, value):
        time.sleep(2)
        self.clearField(self._search_box)
        time.sleep(2)
        self.sendKeys(value, self._search_box)


    def pressEnter(self, value):
        self.sendKeys(value, self._search_box)


    _sku = "//div[@class='sc-ifAKCX cZFrkc']//div[1]//span[@class='sc-dnqmqq QqDcF']"

    def skuSearch(self):
        time.sleep(2)
        self.clickFirstCell()
        time.sleep(2)
        sku_text = self.getText(self._sku)
        time.sleep(1)
        self.elementClick(self._submenu_click)
        time.sleep(2)
        self.EnterProductName(sku_text)
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(2)
        self.clickFirstCell()
        time.sleep(5)
        sku_detail_text = self.getText(self._sku)
        time.sleep(2)
        self.verifyTextContains(actualText=sku_text, expectedText=sku_detail_text)
        self.elementClick(self._submenu_click)
        time.sleep(2)
        sku_text = sku_text[:-1]
        self.EnterProductName(sku_text) # enter product using last text trim
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(2)
        self.clickFirstCell()
        time.sleep(5)
        removed_last_sku = self.getText(self._sku)
        removed_last_sku = removed_last_sku[:-1]
        time.sleep(2)
        self.verifyTextContains(actualText=sku_text, expectedText=removed_last_sku)
        self.elementClick(self._submenu_click)
        time.sleep(2)
        sku_text = sku_text[1:]


        # enter product using first text trim
        self.EnterProductName(sku_text)
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(2)
        self.clickFirstCell()
        time.sleep(5)
        removed_first_sku = self.getText(self._sku)
        removed_first_sku = removed_first_sku[1:]
        removed_first_sku = removed_first_sku[:-1]
        time.sleep(2)
        self.verifyTextContains(actualText=sku_text, expectedText=removed_first_sku)
        time.sleep(2)
        sku_text1 = self.getText(self._sku)
        sku_text1 = sku_text1.lower()
        self.elementClick(self._submenu_click)
        time.sleep(2)


        # enter product using lower case
        self.EnterProductName(sku_text1)
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(3)
        self.clickFirstCell()
        time.sleep(5)
        lower_sku = self.getText(self._sku)
        lower_sku = lower_sku.lower()
        time.sleep(2)
        self.verifyTextContains(actualText=sku_text1, expectedText=lower_sku)


    # Verify tag selected from left side should show expected list accordingly.

    _bulk_tag = '''//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div[contains(text(),'')]'''
    collection_see_more = "//div[@id='root']/div/div[3]/div/div/div[2]/div/div/div[3]/ul/li[7]/span"

    def filterTagVerification(self):
        time.sleep(2)
        self.elementClick(self._submenu_click)
        time.sleep(2)
        self.clearField(self._search_box)
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        time.sleep(2)
        if self.isElementPresent(self.collection_see_more) == True:
            self.elementClick(self.collection_see_more)
        time.sleep(2)
        self.elementClick(self._filter_click)
        time.sleep(2)
        bulk_1 = self.getText(self._filter_click)
        time.sleep(2)
        bulk_tag_text = self.getText(self._bulk_tag)
        time.sleep(2)
        self.verifyTextContains(actualText=bulk_tag_text, expectedText=bulk_1)

    _bulk_2 = "//label[contains(.,'Bulk 2.0')]"

    def filterTagBulk2(self):
        time.sleep(2)
        self.elementClick(self._clear_filter)
        time.sleep(2)
        self.elementClick(self._bulk_2)
        name = self.getText(self._bulk_2)
        time.sleep(2)
        bulk_tag_text = self.getText(self._bulk_tag)
        time.sleep(2)
        self.verifyTextContains(actualText=bulk_tag_text, expectedText=name)

    _custom_tag = "//label[contains(text(),'Custom')]"

    def filterTagCustom(self):
        time.sleep(2)
        self.elementClick(self._clear_filter)
        time.sleep(2)
        self.elementClick(self._custom_tag)
        name = self.getText(self._custom_tag)
        time.sleep(2)
        bulk_tag_text = self.getText(self._bulk_tag)
        time.sleep(2)
        self.verifyTextContains(actualText=bulk_tag_text, expectedText=name)

    _pacific_core_tag = "//label[contains(text(),'Pacific core')]"

    def filterTagPacificCore(self):
        time.sleep(2)
        self.elementClick(self._clear_filter)
        time.sleep(2)
        self.elementClick(self._pacific_core_tag)
        name = self.getText(self._pacific_core_tag)
        time.sleep(2)
        bulk_tag_text = self.getText(self._bulk_tag)
        time.sleep(2)
        self.verifyTextContains(actualText=bulk_tag_text, expectedText=name)

    _phoenix_tag = "//label[contains(text(),'Phoenix')]"

    def filterTagPhoenix(self):
        time.sleep(2)
        self.elementClick(self._clear_filter)
        time.sleep(2)
        self.elementClick(self._phoenix_tag)
        name = self.getText(self._phoenix_tag)
        time.sleep(2)
        bulk_tag_text = self.getText(self._bulk_tag)
        time.sleep(2)
        self.verifyTextContains(actualText=bulk_tag_text, expectedText=name)



    # GC- Sort button

    '''
    
    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Scroll down to 'Phoenix global catalog' and click on the 'browse Global Catalog' picture 
    3) Locate the sort option

    Expected Result
    'Most Relevant' option should be available at the top right corner of the screen next to the Search box
    - All the options under sort should be selectable and should get applied when selected accordingly (.i.e Most relevant, Sort by lowest price, Sort by highest price)

    '''

    _click_most_relevant_dropdown = "//div[@id='root']//div[contains(text(),'Most')]"
    _click_sort_by_lowest = "//div[@id='root']//div[contains(text(),'Sort by lowest price')]"
    _click_sort_by_highest = "//div[@id='root']//div[contains(text(),'Sort by highest price')]"
    #_click_sort_by_highest = "//div[@id='react-select-2-option-2']"

    def pressDownKey(self, value):
        self.sendKeys(value, self._click_most_relevant_dropdown)

    def pressEnterSortSelection(self, value):
        self.sendKeys(value, self._click_most_relevant_dropdown)

    def clickSortLowestDropdown(self):
        time.sleep(4)
        self.elementClick(self._clear_filter)
        time.sleep(2)
        self.elementClick(self._click_most_relevant_dropdown)
        time.sleep(5)
        a = self.elementClick(self._click_sort_by_lowest)
        self.log.info(a)
        time.sleep(4)
        self.log.info("hi this is a print")
        a = "//body/div[@id='root']//div"
        c = '/div[1]/div[2]/div[1]//span[1]'
        list = []
        for i in range(2,25):
            x = [i]
            price_xpath = a + str(x) + c
            time.sleep(4)
            if self.isElementPresent(price_xpath) == False:
                break
            else:
                price = self.getText(price_xpath)
                price = price.replace("$", '')
                price = price.replace(",", '')
                list.append(float(price))

        self.log.info("Original list : " + str(list))
        # using all() to
        # check sorted list
        flag = 0
        if (list == sorted(list)):
            flag = 1
        # printing result
        if (flag):
            self.log.info("Yes, List is sorted.")
            return True
        else:
            self.log.info("No, List is not sorted.")
            return False

    def sortHighest(self):
        time.sleep(4)
        self.elementClick(self._click_sort_by_lowest)
        time.sleep(2)
        self.elementClick(self._click_sort_by_highest)
        time.sleep(3)
        a = "//body/div[@id='root']//div"
        c = '/div[1]/div[2]/div[1]//span[1]'
        list = []
        for i in range(2, 25):
            x = [i]
            price_xpath = a + str(x) + c
            time.sleep(2)
            if self.isElementPresent(price_xpath) == False:
                break
            else:
                price = self.getText(price_xpath)
                price = price.replace("$", '')
                price = price.replace(",", '')
                list.append(float(price))

        self.log.info(list)
        flag = 0
        if (list == sorted(list, reverse=True)):
            flag = 1
        if (flag):
            self.log.info("Yes, List is sorted.")
            return True
        else:
            self.log.info("No, List is not sorted.")
            return False


    # GC - Home button

    '''
    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Scroll down to 'Phoenix global catalog' and click on the 'browse Global Catalog' picture 
    3) Click on the Home button just below the Furnish logo

    Expected Result
    User should get redirected to the Project Dashboard screen
    
    '''


    home_submenu = "//span[contains(.,'Home')]"
    home_navigation_check = "//p[contains(text(),'Your projects')]"

    def clickHomeSubMenu(self):
        time.sleep(2)
        self.elementClick(self.home_submenu)
        time.sleep(2)
        home_text = self.getText(self.home_navigation_check)
        time.sleep(2)
        expected = "Your projects"
        self.verifyTextContains(actualText=home_text, expectedText=expected)


    def clickHomeProductDetail(self):
        time.sleep(2)
        self.waitForElement(self._click_first_img)
        self.elementClick(self._click_first_img)
        time.sleep(2)
        self.elementClick(self._first_cell)
        time.sleep(2)
        self.clickHomeSubMenu()


    # GC - Product spec button
    # Verify product specification button on detail page.

    '''
        Steps
        1) Login to the web app with valid email and proceed to the Dashboard
        2) Scroll down to 'Phoenix global catalog' and click on the 'browse Global Catalog' picture 
        3) Click on any product to go to detail page
        4) Check product specification button 

        Expected Result
        User should see production spec button on global catalog product detail page.

    '''

    _click_product_Specification_button = "//span[contains(text(),'Copy product specs')]"

    def checkSpecButtonDetailPage(self):
        time.sleep(2)
        self.waitForElement(self._click_first_img)
        self.elementClick(self._click_first_img)
        time.sleep(2)
        self.elementClick(self._first_cell)
        time.sleep(2)
        button_name = self.getText(self._click_product_Specification_button)
        self.verifyTextContains(actualText=button_name, expectedText='Copy product specs')


    # GC - Log Out

    '''
    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Scroll down to 'Phoenix global catalog' and click on the 'browse Global Catalog' picture
    3) Click on the user's photo in the header

    Expected Result
    User's name & Logout option should be displayed 
    - On clicking the Logout option, user should get logged out from the app
    
    '''

    _logout_link = "//li[contains(text(),'Logout')]"
    _after_logout_google_text = "//div[@class='auth0-lock-social-button-text']"

    def clickLogout(self):
        time.sleep(2)
        self.elementClick(self.home_submenu)
        time.sleep(2)
        self.waitForElement(self._click_first_img)
        self.elementClick(self._click_first_img)
        time.sleep(2)
        self.waitForElement(self._user_profile_icon)
        self.elementClick(self._user_profile_icon)
        time.sleep(2)
        self.elementClick(self._logout_link)
        time.sleep(4)
        text = self.getText(self._after_logout_google_text)
        text_name = 'Log in with Google'
        time.sleep(2)
        self.verifyTextContains(actualText=text, expectedText=text_name)

