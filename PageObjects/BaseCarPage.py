import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage
from Utilities import configReader


class BaseCarPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH,configReader.readConfig("webelements", "carTitle")).text

    def getCarPriceAndName(self):
        carname = self.driver.find_elements(By.XPATH, configReader.readConfig("webelements", "carName"))
        carprice = self.driver.find_elements(By.XPATH, configReader.readConfig("webelements", "carPrice"))
        for i in range(1,len(carprice)):
            print(carname[i].text," price is :  "+str(carprice[i].text))

    def filterCarsbyBudget(self):
        self.click("make_XPATH")
        time.sleep(5)

        self.click("budget_XPATH")
        self.sliderDragAndDrop("budgetSlider_XPATH","250","0")
        carpricemax = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", "budgetSliderMax_Xpath"))

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='o-bUVylL o-dsiSgT o-fznJzu o-fznJPk o-fznVqX o-fznVsN xc8GmL o-cpnuEd'] button[type='button']"))
        )
        element.click()

        time.sleep(10)

    def getCarPrice(self):
        carprice = self.driver.find_elements(By.XPATH, configReader.readConfig("webelements", "carPrice_XPATH"))
        return carprice

    def getPriceRange(self):
        carprice = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", "priceRange_XPATH"))
        carpricelist = carprice.text.split(" ")
        carpricerange = carpricelist[0].split("-")
        return carpricerange
