import time
from base.selenium_driver import SeleniumDriver


class login(SeleniumDriver):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''
    Add all the locators that will be used for login and logout screens.
    '''
    # Locators:

    _google_login_button = "//div[@class='auth0-lock-social-button-text']"
    _email_id_textfield = "//input[@id='identifierId']"
    _next_button = "//span[contains(text(),'Next')]"
    _password_textfield = "//input[@name='password']"
    _user_profile_icon = "//img[contains(@src,'https://lh4.googleusercontent.com/-l0Nse9g06Lk/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3reoOmkz5csX7CYFMarjSm6XD9HFwQ/photo.jpg')]"
    _logout_link = "//li[contains(text(),'Logout')]"

    # Relogin test locators for google.
    _cache_login = "//div[@id='profileIdentifier']"
    _another_user = "//div[@class='BHzsHc']"

    # wrong password entered
    _login_validation = "//span[contains(text(),'Wrong password. Try again or click Forgot password')]"

    '''
    Create a dynamic method for each the locator so that if 
    anytime locator id changed so we need to change it only on locators
    
    '''

    def clickGoogleLoginButton(self):
        self.waitForElement(self._google_login_button)
        self.elementClick(self._google_login_button)

    def enterEmail(self, email):
        self.waitForElement(email, self._email_id_textfield)
        self.sendKeys(email, self._email_id_textfield)

    def clickNextButton(self):
        self.waitForElement(self._next_button)
        self.elementClick(self._next_button)

    def enterPassword(self, password):
        self.waitForElement(password,self._password_textfield)
        self.sendKeys(password,self._password_textfield)

    def clickUserProfileIcon(self):
        time.sleep(5)
        self.elementClick(self._user_profile_icon)

    def clickLogoutLink(self):
        time.sleep(5)
        self.elementClick(self._logout_link)

    def clickCache(self):
        self.elementClick(self._cache_login)

    def anotherUserLogin(self):
        self.elementClick(self._another_user)

    def validationText(self):
        self.elementClick(self._login_validation)


    # First time user login
    def validloginForm(self, email="", password=""):
        self.clickGoogleLoginButton()
        time.sleep(2)
        self.enterEmail(email)
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.enterPassword(password)
        time.sleep(2)
        self.clickNextButton()

    def loginfail(self, email="", password=""):
        self.enterEmail(email)
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.enterPassword(password)
        time.sleep(2)
        self.clickNextButton()

    # Login user again using self google cookies option
    def loginCache(self):
        self.clickGoogleLoginButton()
        time.sleep(2)
        self.clickCache()

    # login user using using google another option
    def anotherUser(self):
        self.clickGoogleLoginButton()
        time.sleep(2)
        self.anotherUserLogin()

    # Logout function
    def logout(self):
        time.sleep(5)
        self.clickUserProfileIcon()
        self.clickLogoutLink()

    def loginValidation(self):
        validation_Text = "Wrong password. Try again or click Forgot password to reset it."
        message = self.getText(self._login_validation)
        self.verifyTextContains(actualText=message, expectedText=validation_Text)

















