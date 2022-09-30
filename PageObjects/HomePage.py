import time

from PageObjects.BasePage import BasePage
from PageObjects.NewcarsPage import NewcarsPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newcars_XPATH")
        self.click("findnewcars _XPATH")
        time.sleep(5)
        return NewcarsPage(self.driver)