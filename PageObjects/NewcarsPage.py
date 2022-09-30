from PageObjects.BasePage import BasePage


class NewcarsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectHonda(self):
        self.click("honda_XPATH")

    def selectBmw(self):
        self.click("bmw_XPATH")
