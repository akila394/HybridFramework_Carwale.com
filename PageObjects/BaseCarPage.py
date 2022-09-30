from selenium.webdriver.common.by import By
from Utilities import configReader


class BaseCarPage:
    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH,configReader.readConfig("webelements", "carTitle")).text

    def getCarPriceAndName(self):
        carname = self.driver.find_elements(By.XPATH, configReader.readConfig("webelements", "carName"))
        carprice = self.driver.find_elements(By.XPATH, configReader.readConfig("webelements", "carPrice"))

        for i in range(1,len(carprice)):
            print(carname[i].text," price is :  "+str(carprice[i].text))