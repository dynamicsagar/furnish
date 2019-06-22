import time
from base.selenium_driver import SeleniumDriver


class projectcard(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # project_card
    # Locators

    '''
    listing pages 
            Getting budget values
    '''
    _budget_conditions = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/span[1]"
    _budget_allocated = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/span[2]"
    _estimated_total = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/span[2]"
    # Project name
    _title_name = "//p[contains(text(),'Hareza Ikebukuro - P1')]"

    #pagination next
    _next = "//li[contains(text(),'Next')]"

    #pagination count
    _total_count = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[8]"

    #title name
    _element_name = "//p[contains(text(),'Central Plaza - P1')]"

    #edit address link on detail page
    edit_address = "//a[@class='budget-card-edit__anchor']"

    # edit address text
    element = "//p[contains(text(),'Furniture budget')]"

    # add budget
    _budget_field = "//input[@placeholder='$0.00']"

    #save button
    _save_button = "//span[contains(text(),'Save')]"

    # values of budget, subtotal
    _subtotal = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[4]/p[2]"
    _budget = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[3]/p[2]"
    _budget_met = "//span[@class='sc-sdtwF czaRpr']"
    sa = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]"
    _add_budget_button = "//a[@class='budget-card-add']"
    _home_menu = "//span[contains(text(),'Home')]"


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
        if self.isElementPresent(self._add_budget_button) == True:
            self.elementClick(self._add_budget_button)
            self.EnterBudget('11024.60')
            self.clickSaveButton()
        else:
            self.addEditBudget()
            time.sleep(2)
            value = '-123'
            self.EnterBudget('-123')
            time.sleep(2)
            self.clickSaveButton()
            time.sleep(2)
            neg_value = self.getText(self._budget)
            if neg_value != value:
                return True
            else:
                return False

    # Finding specific post using loop
    def loop(self):
        time.sleep(15)
        self.waitForElement(self._total_count)
        count = int(self.getText(self._total_count))
        print(count)
        for i in range(count):
            time.sleep(2)
            element_name = "Central Plaza - P1"
            textname = self.getText(self._element_name)
            if element_name == textname:
                break
            else:
                next_link = self.getElement(self._next)
                next_link.click()
        self.elementClick(self._element_name)

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
        subtotal = subtotal.replace('$', '')
        time.sleep(2)
        self.addEditBudget()
        time.sleep(2)
        self.EnterBudget(subtotal)
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(2)
        t = self.getText(self.sa)
        self.verifyTextContains(actualText=t, expectedText='Budget met!')
        '''if t == s:
            return True
        else:
            return False'''

    def budgetOver(self):
        self.addBudget()
        time.sleep(5)
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
        trim1 = self.getText(self.sa)
        trim1 = trim1.split()
        trim1 = trim1[1]
        self.verifyTextContains(actualText=trim1, expectedText="over")

    def budgetUnder(self):
        self.addBudget()
        time.sleep(5)
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
        trim1 = self.getText(self.sa)
        trim1 = trim1.split()
        trim1 = trim1[1]
        self.verifyTextContains(actualText=trim1, expectedText="under")

    # locators:
    _close_project_details = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[5]/span[1]"

    # Click on project link to minimise it.
    def closeProjectLink(self):
        time.sleep(5)
        self.elementClick(self._close_project_details)
        time.sleep(2)
        value = "Expand project details"
        get_value = self.getText(self._close_project_details)
        self.verifyTextContains(actualText=get_value, expectedText="Expand project details")
        '''if get_value == value:
            return True
        else:
            return False'''

    # Click on project link to maximise it.
    def expandProjectLink(self):
        time.sleep(5)
        self.elementClick(self._close_project_details)
        time.sleep(2)
        value = "Close project details"
        get_value = self.getText(self._close_project_details)
        self.verifyTextContains(actualText=get_value, expectedText="Close project details")

    # locators:
    _button_status = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]"
    _outer_button_status = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    _first_notstarted = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]"
    _second_inprogress = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]"
    _third_done = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]"
    _fourth_blocked = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]"
    _first_project = "//body/div[@id='root']/div[@class='sc-hZSUBg bopQAN']/div[@class='sc-iuJeZd faqmZA']/div[@class='sc-cmthru dibNUQ']/div[@class='sc-gbOuXE ckrwfa sc-cmTdod bWGGJA']" \
                     "/div[@class='sc-lhVmIH hJmtbF']/div[@class='sc-jwKygS faoqUI']/div[1]"


    def clickFirstProject(self):
        time.sleep(5)
        self.waitForElement(self._first_project)
        time.sleep(2)
        self.elementClick(self._first_project)

    def projectStage(self):
        time.sleep(5)
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


    def projectStageChange1(self):
        time.sleep(5)
        self.loop()
        time.sleep(2)
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._second_inprogress)
        time.sleep(5)
        aa = self.getText(self._button_status)
        time.sleep(5)
        self.elementClick(self._home_menu)
        time.sleep(2)
        bb = self.getText(self._outer_button_status)
        time.sleep(2)
        self.verifyTextContains(actualText=aa, expectedText=bb)

    def projectStageChange2(self):
        time.sleep(5)
        self.loop()
        time.sleep(2)
        self.elementClick(self._button_status)
        time.sleep(2)
        self.elementClick(self._fourth_blocked)
        time.sleep(2)
        text = self.getText(self._button_status)
        time.sleep(5)
        self.elementClick(self._home_menu)
        time.sleep(5)
        text1 = self.getText(self._outer_button_status)
        self.verifyTextContains(actualText=text, expectedText=text1)

    def projectStageChange3(self):
        time.sleep(5)
        self.loop()
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
        self.waitForElement(self._stargate_link_detail_page)
        window_before = self.driver.window_handles[0]
        self.elementClick(self._stargate_link_detail_page)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.isElementDisplayed(self._stargate_site_logo)
        return True






















