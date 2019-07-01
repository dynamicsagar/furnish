import time
from base.selenium_driver import SeleniumDriver


class CatalogPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # 01 TC: Access the Catalog page
    '''
    
    Preconditions
    Pre-requisite: 1 When a few Products are assigned to project 
    Pre-requisite: 2 When no Products are assigned to project

    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Click on the any Project 
    3) Click on 'Add more products' button

    Expected Result
    User should get redirected to the Catalog page (i.e Home >Project Name> Catalog)
    
    '''

    _click_project = "//p[contains(text(),'12 Calle de Prim - P1')]"
    _add_more_product = "//span[contains(text(),'Add more products')]"
    _project_title_name = "//p[@class='project-title']"
    _product_name_submenu = "//span[3][contains(text(),'12 Calle de Prim - P1')]"
    _catalog_submenu = "//span[contains(.,'Catalog')]"
    _shop_for_more_link = "//a[contains(text(),'+ Shop for more')]"
    home_submenu = "//span[contains(.,'Home')]"
    home_navigation_check = "//p[contains(text(),'Your projects')]"
    _user_profile_icon = "//img[contains(@src,'https://lh4.googleusercontent.com/-l0Nse9g06Lk/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3reoOmkz5csX7CYFMarjSm6XD9HFwQ/photo.jpg')]"
    _logout_link = "//li[contains(text(),'Logout')]"
    _after_logout_google_text = "//div[@class='auth0-lock-social-button-text']"


    def accessCatalogPage(self):
        time.sleep(15)
        self.waitForElement(self._click_project)
        self.elementClick(self._click_project)
        time.sleep(2)
        title_name = self.getText(self._project_title_name)
        time.sleep(2)
        self.waitForElement(self._add_more_product)
        self.elementClick(self._add_more_product)
        time.sleep(2)
        product_name_submenu = self.getText(self._product_name_submenu)
        time.sleep(2)
        self.verifyTextContains(actualText=title_name, expectedText=product_name_submenu)
        self.catalogMenuVerification()


    def catalogMenuVerification(self):
        catalog_submenu = self.getText(self._catalog_submenu)
        catalog_text = 'Catalooog'
        time.sleep(2)
        self.verifyTextContains(actualText=catalog_submenu, expectedText=catalog_text)

    # 02 TC - Access the Catalog page from search for product button

    '''
    Preconditions
    Pre-requisite: When no Product is assinged to project

    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Click on the any Project 
    3) Click on 'Search for products' button

    Expected Result
    User should get redirected to the Catalog page (i.e Home >Project Name> Catalog)
    
    '''

    def accessCatalogPageSearchFromProduct(self):
        time.sleep(2)
        self.elementClick(self._product_name_submenu)
        time.sleep(2)
        link_text = self.getText(self._shop_for_more_link)
        link_text_name = "+ Shop for more"
        time.sleep(2)
        self.verifyTextContains(actualText=link_text, expectedText=link_text_name)
        time.sleep(2)
        self.elementClick(self._shop_for_more_link)
        time.sleep(2)
        self.catalogMenuVerification()


    # 03 TC - Catalog - Home button
    '''
    Preconditions
    Pre-requisite: 1 When a few Products are assigned to project 
    Pre-requisite: 2 When no Products are assigned to project

    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Click on the any Project 
    3) Click on 'Add more product' button
    4) Click on the Home button just below the Furnish logo

    Expected Result
    User should get redirected to the Project Dashboard screen

    '''

    def navigateHomePage(self):
        time.sleep(2)
        home_text = self.getText(self.home_submenu)
        home_text_name = "Home"
        self.verifyTextContains(actualText=home_text, expectedText=home_text_name)
        time.sleep(2)
        self.elementClick(self.home_submenu)
        time.sleep(2)
        home_navigation = self.getText(self.home_navigation_check)
        home_your_project_text = 'Your projects'
        self.verifyTextContains(actualText=home_navigation, expectedText=home_your_project_text)


    # 04 TC - Catalog- Log Out

    '''
    
    Preconditions
    Pre-requisite: 1 When a few Products are assigned to project 
    Pre-requisite: 2 When no Products are assigned to project

    Steps
    1) Login to the web app with valid email and proceed to the Dashboard
    2) Click on the any Project 
    3) Click on 'Add more product' button
    4) Click on the user's photo in the header

    Expected Result
    User's name & Logout option should be displayed 
    - On clicking the Logout option, user should get logged out from the app & redirected to the login page i.e. "LOG IN WITH GOOGLE"
   
    '''

    def clickLogout(self):
        self.waitForElement(self._click_project)
        self.elementClick(self._click_project)
        time.sleep(2)
        self.waitForElement(self._add_more_product)
        self.elementClick(self._add_more_product)
        time.sleep(2)
        self.waitForElement(self._user_profile_icon)
        self.elementClick(self._user_profile_icon)
        time.sleep(2)
        self.elementClick(self._logout_link)
        time.sleep(5)
        text = self.getText(self._after_logout_google_text)
        text_name = 'Log in with Google'
        time.sleep(3)
        self.verifyTextContains(actualText=text, expectedText=text_name)


























