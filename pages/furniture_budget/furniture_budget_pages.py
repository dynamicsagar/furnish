import time
from base.selenium_driver import SeleniumDriver
from pages.add_remove_product.add_remove_product_page import addRemoveProducts


class FurnitureBudget(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # project_card
    # Locators

    '''
    listing pages Getting budget values
            
    '''

    # Project name
    _title_name = "//p[contains(text(),'Hareza Ikebukuro - P1')]"
    _click_first_project = "//p[contains(text(),'Avenida Circunvalacion del Club Golf Los Incas 170')]"
    _bar = "//div[1]/div[5]/div[1]/span[1]"

    # pagination next
    _next = "//li[contains(text(),'Next')]"

    # pagination count
    _total_count = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[8]"

    # title name
    _element_name = "//p[contains(text(),'Central Plaza - P1')]"

    # edit address link on detail page
    edit_address = "//a[@class='budget-card-edit__anchor']"

    # edit address text
    element = "//p[contains(text(),'Furniture budget')]"

    # add budget
    _budget_field = "//input[@placeholder='$0.00']"

    # save button
    _save_button = "//span[contains(text(),'Save')]"

    # values of budget, subtotal
    _subtotal = "//div[@id='project-page-header-container']//div[3]//div[4]//p[2]"
    _budget = "//div[@id='project-page-header-container']//div[3]//div[3]//p[2]"
    _budget_met = "//div[@id='project-page-header-container']//div[3]//div[2]"
    _add_budget_button = "//a[@class='budget-card-add']"
    _home_menu = "//span[contains(.,'Home')]"


    '''
    
    1. Login to web app
    2. Click on any product
    --- Check budget link available or not
    if available - click on budget link
    
    
    '''


    # Check if budget link is available then click on budget link else return to function.

    def addBudget(self):
        time.sleep(3)
        if self.isElementPresent(self._add_budget_button) == True:
            self.elementClick(self._add_budget_button)
            self.EnterBudget('11024.60')
            self.clickSaveButton()
        else:
            return

    # Enter Budget value using add budget link

    def enterBudget(self):
        time.sleep(2)
        self.waitForElement(self._click_first_project)
        self.elementClick(self._click_first_project)
        time.sleep(2)

        if self.isElementPresent(self._add_budget_button) == True:
            self.elementClick(self._add_budget_button)
            self.EnterBudget('11024.60')
            self.clickSaveButton()
        else:
            self.addEditBudget()
            time.sleep(2)
            self.EnterBudget('0')
            time.sleep(2)
            self.clickSaveButton()
            time.sleep(2)
            self.addBudget()

    # Enter negative value and verify it does not take it.

    def enterNegativeValue(self):
        time.sleep(3)
        if self.isElementPresent(self._add_budget_button) == True:
            self.log.info('negative value --add budget button available')
            self.elementClick(self._add_budget_button)
            self.EnterBudget('11024.60')
            self.clickSaveButton()
        else:
            self.log.info('negative value enter')
            self.addEditBudget()
            time.sleep(2)
            value = '-123'
            self.EnterBudget(value)
            time.sleep(2)
            self.clickSaveButton()
            time.sleep(2)
            neg_value = self.getText(self._budget)
            self.log.info(neg_value)
            self.log.info('negative value enter')
            if neg_value != value:
                return True
            else:
                return False

    # Edit budget function
    def addEditBudget(self):
        time.sleep(2)
        self.elementClick(self.element)
        time.sleep(2)
        self.elementClick(self.edit_address)
        time.sleep(2)

    # Enter budget function
    def EnterBudget(self, value):
        time.sleep(2)
        self.clearField(self._budget_field)
        time.sleep(2)
        self.sendKeys(value, self._budget_field)

    # save button function to save entered budget
    def clickSaveButton(self):
        self.elementClick(self._save_button)

    # Budget met def to calculate budget met or not.
    def budgetMet(self):
        self.addBudget()
        time.sleep(2)
        subtotal = self.getText(self._subtotal)
        self.ad = addRemoveProducts(self.driver)
        if subtotal == '-':
            self.ad.addRoomAssignment()
        subtotal = self.getText(self._subtotal)
        subtotal = subtotal.replace('$', '')
        time.sleep(2)
        self.webScroll(direction='up')
        self.addEditBudget()
        time.sleep(2)
        self.EnterBudget(subtotal)
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(5)
        t = self.getText(self._budget_met)
        self.verifyTextContains(actualText=t, expectedText='Budget met!')
        time.sleep(2)
        self.elementClick(self._home_menu)
        time.sleep(5)
        bar_text = self.getText(self._bar)
        time.sleep(2)
        self.verifyTextContains(actualText=t, expectedText=bar_text)

    def budgetOver(self):
        self.elementClick(self._click_first_project)
        time.sleep(2)
        self.addBudget()
        time.sleep(2)
        budget = self.getText(self._budget)
        time.sleep(2)
        budget = budget.replace('$', '')
        budget = budget.replace(',', '')
        subtotal = self.getText(self._subtotal)
        subtotal = subtotal.replace('$', '')
        subtotal = subtotal.replace(',', '')
        if budget < subtotal:
            calculate = str(float(subtotal) - float(budget))
            budget = str(float(budget) - float(calculate))
        elif budget > subtotal:
            calculate = str(float(budget) - float(subtotal))
            value = float(5)
            calculate = str(float(calculate) + float(value))
            budget = str(float(budget) - float(calculate))
        elif budget == subtotal:
            value = float(5)
            budget = str(float(budget) - float(value))

        time.sleep(2)
        self.addEditBudget()
        time.sleep(2)
        self.EnterBudget(str(budget))
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(3)
        trim1 = self.getText(self._budget_met)
        trim1 = trim1.split()
        trim1 = trim1[1]
        self.verifyTextContains(actualText=trim1, expectedText="over")
        time.sleep(2)
        self.elementClick(self._home_menu)
        time.sleep(4)
        bar_text = self.getText(self._bar)
        time.sleep(2)
        self.verifyTextContains(actualText=bar_text, expectedText='$5.00 over')


    def budgetUnder(self):
        self.elementClick(self._click_first_project)
        time.sleep(2)
        self.addBudget()
        time.sleep(2)
        budget = self.getText(self._budget)
        time.sleep(2)
        budget = budget.replace('$', '')
        budget = budget.replace(',', '')
        subtotal = self.getText(self._subtotal)
        subtotal = subtotal.replace('$', '')
        subtotal = subtotal.replace(',', '')
        if budget < subtotal:
            calculate = str(float(subtotal) - float(budget))
            value = float(5)
            calculate = str(float(calculate) + float(value))
            budget = str(float(budget) + float(calculate))
        elif budget > subtotal:
            calculate = str(float(budget) - float(subtotal))
            budget = str(float(budget) + float(calculate))
        elif budget == subtotal:
            value = float(5)
            budget = str(float(budget) + float(value))

        time.sleep(2)
        self.addEditBudget()
        time.sleep(2)
        self.EnterBudget(str(budget))
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(3)
        trim1 = self.getText(self._budget_met)
        trim1 = trim1.split()
        trim1 = trim1[1]
        self.verifyTextContains(actualText=trim1, expectedText="under")
        time.sleep(2)
        self.elementClick(self._home_menu)
        time.sleep(4)
        bar_text = self.getText(self._bar)
        time.sleep(2)
        self.verifyTextContains(actualText=bar_text, expectedText='$5.00 under')


    # locators:
    _close_project_details = "//span[contains(text(),'Close project details')]"
    _expand_project_details = "//span[contains(text(),'Expand project details')]"

    # Click on project link to minimise it.
    def closeProjectLink(self):
        time.sleep(2)
        self.elementClick(self._click_first_project)
        time.sleep(5)
        self.elementClick(self._close_project_details)
        time.sleep(2)
        value = "Expand project details"
        get_value = self.getText(self._expand_project_details)
        time.sleep(2)
        self.verifyTextContains(actualText=get_value, expectedText="Expand project details")

    # Click on project link to maximise it.
    def expandProjectLink(self):
        time.sleep(5)
        self.elementClick(self._expand_project_details)
        time.sleep(2)
        value = "Close project details"
        get_value = self.getText(self._close_project_details)
        time.sleep(2)
        self.verifyTextContains(actualText=get_value, expectedText=value)

    # locators:

    _button_status = "//div[@id='project-page-header-container']/div[1]"
    _outer_button_status = '''//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]'''
    _first_notstarted = "//div[@id='project-page-header-container']/div[2]/div/div[2]/p"
    _second_inprogress = "//div[@id='project-page-header-container']/div[2]/div/div[1]/p"
    _third_done = "//div[@id='project-page-header-container']/div[2]/div/div[3]/p"
    _fourth_blocked = "//div[@id='project-page-header-container']/div[2]/div/div[4]/p"

    def projectStage(self):
        time.sleep(2)
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._third_done)
        time.sleep(5)
        a = self.getText(self._button_status)
        time.sleep(5)
        self.elementClick(self._home_menu)
        time.sleep(2)
        b = self.getText(self._outer_button_status)
        self.verifyTextContains(actualText=a, expectedText=b)

    def projectStatus1(self):
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._second_inprogress)
        time.sleep(3)
        aa = self.getText(self._button_status)
        time.sleep(3)
        self.elementClick(self._home_menu)
        time.sleep(5)
        outer_button_status = self.getText(self._outer_button_status)
        time.sleep(2)
        self.verifyTextContains(actualText=aa, expectedText=outer_button_status)

    def projectStatus2(self):
        self.elementClick(self._click_first_project)
        time.sleep(3)
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._fourth_blocked)
        time.sleep(3)
        text = self.getText(self._button_status)
        time.sleep(2)
        self.elementClick(self._home_menu)
        time.sleep(5)
        obs = self.getText(self._outer_button_status)
        self.verifyTextContains(actualText=text, expectedText=obs)

    def projectStatus3(self):
        self.elementClick(self._click_first_project)
        time.sleep(2)
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._first_notstarted)
        time.sleep(2)
        aaa = self.getText(self._button_status)
        time.sleep(5)
        self.elementClick(self._home_menu)
        time.sleep(5)
        bbb = self.getText(self._outer_button_status)
        self.verifyTextContains(actualText=aaa, expectedText=bbb)

    # LOCATORS

    # stargate link on detail page
    _stargate_link_detail_page = "//span[@class='stargate']"

    # stargate page logo
    _stargate_site_logo = "//img[@id='login-logo']"

    # Click on stargate link to verify link navigation and check navigation is going correct.


    def clickStargateLink(self):
        time.sleep(2)
        self.waitForElement(self._click_first_project)
        self.elementClick(self._click_first_project)
        time.sleep(2)
        self.waitForElement(self._stargate_link_detail_page)
        window_before = self.driver.window_handles[0]
        self.elementClick(self._stargate_link_detail_page)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.isElementDisplayed(self._stargate_site_logo)
        return True






















