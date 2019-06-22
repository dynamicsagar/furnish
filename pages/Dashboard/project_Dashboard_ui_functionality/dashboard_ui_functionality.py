import time
from base.selenium_driver import SeleniumDriver


class dashboard(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    _project_card = "//p[contains(text(),'12 Calle de Prim - P1')]"
    _card_name = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]"
    _detail_page_card_name = "//p[@class='project-title']"
    _opening = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/span[1]'''
    _floor_count = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[4]/span[1]'''
    _bar = "//div[1]/div[5]/div[1]/span[1]"
    _budget_allocated = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[6]/span[1]'''
    _estimated_total = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[7]/span[1]'''
    _project_status = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]'''

    # 01 TC - Verify Opening Text in grid
    def openingText(self):
        time.sleep(10)
        self.waitForElement(self._opening)
        opening_text = self.getText(self._opening)
        opening_text_name = 'Opening'
        time.sleep(2)
        self.verifyTextContains(actualText=opening_text, expectedText=opening_text_name)

    # 02 TC - Verify floor Text in grid
    def floorCount(self):
        time.sleep(2)
        floor_text = self.getText(self._floor_count)
        floor_text_name = 'Floor count'
        self.verifyTextContains(actualText=floor_text, expectedText=floor_text_name)

    # 03 TC - Verify bar in grid
    def bar(self):
        time.sleep(2)
        bar_text = self.getText(self._bar)
        a = bar_text.split()
        self.log.info(a)
        time.sleep(2)
        for i in a:
            if i == 'under' or i == 'over' or i == '-':
                self.log.info('hi')
            else:
                self.log.info('fail')
        return True

    # 04 TC - Verify budget allocated text in grid
    def budgetAllocated(self):
        time.sleep(2)
        budget_text = self.getText(self._budget_allocated)
        budget_text_name = 'Budget allotted'
        time.sleep(2)
        self.verifyTextContains(actualText=budget_text, expectedText=budget_text_name)

    # 05 TC - Verify estimated total text in grid
    def estimatedTotal(self):
        time.sleep(2)
        estimated_text = self.getText(self._estimated_total)
        estimated_text_name = 'Estimated total'
        time.sleep(2)
        self.verifyTextContains(actualText=estimated_text, expectedText=estimated_text_name)

    # 06 TC - Verify project status tab in grid
    def projectStatus(self):
        self.isElementPresent(self._project_status)
        return True

    def clickProjectCard(self):
        self.elementClick(self._project_card)

    def detailCardName(self):
        self.getText(self._detail_page_card_name)

    def projectCardToProjectDetail(self):
        time.sleep(5)
        self.waitForElement(self._card_name)
        time.sleep(2)
        sa = self.getText(self._project_card)
        time.sleep(2)
        self.clickProjectCard()
        time.sleep(2)
        detail_project_card_name = self.getText(self._detail_page_card_name)
        time.sleep(1)
        self.verifyTextContains(actualText=sa, expectedText=detail_project_card_name)

    # TC  2 : Verify that pagination functions accordingly

    _page2_pagination = "//li[contains(text(),'2')]"
    _next = "//li[contains(text(),'Next')]"
    _back = "//li[contains(text(),'Back')]"
    _home_menu = "//span[contains(text(),'Home')]"

    def clickFurnishIcon(self):
        time.sleep(2)
        self.elementClick(self._home_menu)

    def scroll(self):
        self.clickFurnishIcon()
        time.sleep(4)
        self.webScroll(direction='down')
        '''scroll = self.getElement(self._scroll_to_element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -350);")'''

    '''def nextpag(self):
        pages_remaining = True
        while pages_remaining:
            # DO YOUR THINGS WITHIN THE PAGE
            try:
                # Checks if there are more pages with links
                next_link = self.getElement(self._next)
                next_link.click()
                time.sleep(5)
            except:
                rows_remaining = False'''

    def clickPagination(self):
        self.scroll()
        time.sleep(2)
        element = self.getElement(self._next)
        back_element = self.getElement(self._back)
        if element.is_enabled() == True and back_element.is_enabled() == True:
            self.elementClick(self._next)
            time.sleep(2)
            self.elementClick(self._back)
            return True
        elif element.is_enabled() == True:
            self.elementClick(self._next)
            return True
        elif (element.is_enabled() == False) and (back_element.is_enabled() == False):
            return True
        else:
            return False


    # Verify that Global Catalog page is accessible from the Dashboard page
    #locators

    phoenix_text = "//p[contains(text(),'Phoenix global catalog')]"
    _first_img = "//div[@class='left-top']//img"
    _check_global_catalog_redirection = "//span[contains(.,'Global catalog')]"

    def catalogPage(self):
        time.sleep(3)
        text = self.getText(self.phoenix_text)
        actual_text = 'Phoenix global catalog'
        if actual_text == text:
            self.elementClick(self._first_img)
            time.sleep(2)
            text_re = self.getText(self._check_global_catalog_redirection)
            time.sleep(1)
            self.verifyTextContains(actualText=text_re, expectedText="Global catalog")
        else:
            return False


    # Verify the links navigates properly.
    # Locators

    _article_link = "//a[contains(text(),'this help article')]"
    _navigation_page_header = "//h2[@class='t__h1']"

    def clickArticleLink(self):
        self.elementClick(self._article_link)

    def linkNavigation(self):
        time.sleep(2)
        self.clickFurnishIcon()
        time.sleep(2)
        self.scroll()
        time.sleep(2)
        if self.isElementPresent(self._article_link) == True:
            window_before = self.driver.window_handles[0]
            self.clickArticleLink()
            window_after = self.driver.window_handles[1]

            # switch on to new child window
            self.driver.switch_to.window(window_after)
            self.isElementDisplayed(self._navigation_page_header)
            return True
        else:
            return False


