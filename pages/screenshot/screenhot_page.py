import time
from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class ScreenshotPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _click_project = "//p[contains(text(),'12 Calle de Prim - P1')]"
    _add_more_product = "//span[contains(text(),'Add more products')]"
    _first_cell = '''//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div'''
    _add_assignment = "//div[@id='root']/div/div[3]/div/div/div[3]/div[2]/div[2]/div[2]//a[contains(., 'Assign')]"
    _assign_new_room = "//div[contains(text(),'Assign to new rooms')]"
    _remove_product = "remove product from project"
    _cancel_button_modal_box = "//div[@id='root']/div[3]/div/div/div[3]/div/button/span[contains(text(),'Cancel')]"
    _close_button = "//div//button[@title = 'Close Dialog']"
    _all_rooms = "//span[contains(text(),'All rooms')]"
    _assign_new_product_click = "//div[contains(text(),'Assign new products')]"


    def Home(self):
        time.sleep(15)
        self.ut = Util()
        name = self.ut.getUniqueName(10)
        self.log.info(name)
        self.fullpage_screenshot(name + 'home.png')
        time.sleep(5)
        self.webScroll(direction='up')
        self.webScroll(direction='up')

    def ProjectDetailScreen(self):
        time.sleep(2)
        self.waitForElement(self._click_project)
        self.elementClick(self._click_project)
        time.sleep(5)
        self.fullpage_screenshot('ProjectDetailScreen.png')
        time.sleep(4)
        self.webScroll(direction='up')

    def AssignmentScreen(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.screenShot('AssignmentScreen.png')
        time.sleep(2)

    def AssignmentScreenNewRoom(self):
        self.elementClick(self._assign_new_room)
        self.screenShot('AssignmentnewroomScreen.png')
        time.sleep(2)

    def AssignmentScreenRemoveProduct(self):
        self.elementClick(self._remove_product, locatorType='link')
        time.sleep(2)
        self.screenShot('Removeproductpopup.png')
        time.sleep(2)
        self.elementClick(self._cancel_button_modal_box)
        time.sleep(2)
        self.elementClick(self._close_button)

    def ViewByRoomScreen(self):
        time.sleep(2)
        self.elementClick(self._all_rooms)
        self.screenShot('ViewRoom')

    def ViewByRoomEditScreenPopUP(self):
        time.sleep(2)
        self.elementClick(self._add_assignment)
        time.sleep(2)
        self.screenShot('ViewbytypeEditScreen')
        time.sleep(2)

    def ViewByRoomAssignNewProductScreen(self):
        self.elementClick(self._assign_new_product_click)
        time.sleep(2)
        self.screenShot('ViewbytypeNewProductScreen')
        time.sleep(2)
        self.elementClick(self._close_button)

    def CatalogScreen(self):
        time.sleep(5)
        self.elementClick(self._add_more_product)
        time.sleep(2)
        self.fullpage_screenshot('Catalog.png')
        time.sleep(2)
        self.webScroll(direction='up')
        self.webScroll(direction='up')
        time.sleep(2)

    def CatalogDetailScreen(self):
        self.elementClick(self._first_cell)
        time.sleep(2)
        self.fullpage_screenshot('CatalogDetailScreen.png')
        time.sleep(4)









