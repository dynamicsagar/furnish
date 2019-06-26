import time
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from pages.add_remove_product.add_remove_product_page import addRemoveProducts


class ViewByRoom(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _all_rooms = "//span[contains(text(),'All rooms')]"
    _rooms_dropdown_click = "//div[contains(text(),'View rooms with products')]"
    _thumbnail_icon = "//*[@class='svg-inline--fa fa-th fa-w-16 secondIcon']"






