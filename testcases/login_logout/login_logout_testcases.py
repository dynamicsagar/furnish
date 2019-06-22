from pages.login_and_logout.login_logout_page import login
import utilities.custom_logger as cl
import unittest
import pytest
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = login(self.driver)

    def test_01logout(self):
        self.log.info("*#" * 20)
        self.log.info(" Logout from Dashboard screen ")
        self.log.info("*#" * 20)
        self.lp = login(self.driver)
        self.lp.logout()

    def test_02InvalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("Login with an invalid account ")
        self.log.info("*#" * 20)
        self.lp = login(self.driver)
        self.lp.anotherUser()
        self.lp.loginfail("pankaj@arcgate.com", "Welfdsfsdfsdfcome123!")
        self.lp.loginValidation()



