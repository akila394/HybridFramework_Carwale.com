import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.BaseCarPage import BaseCarPage
from PageObjects.HomePage import HomePage
from Tests.basetest import BaseTest
from Utilities import dataReader
from Utilities.LogUtil import Logger
import logging

log = Logger(__name__, logging.INFO)
class Test_CarWale(BaseTest):

    def test_gotoNewCar(self):
        log.logger.info("*********** Inside the New car Test ************")
        home = HomePage(self.driver)
        home.gotoNewCars()
        allure.attach(self.driver.get_screenshot_as_png(),name="dologin", attachment_type=AttachmentType.PNG)
        log.logger.info("*********** Moved to new cars page successfully *********")
        time.sleep(5)

    @pytest.mark.parametrize("carbrand, carTitle", dataReader.get_data("carbrandtest"))
    def test_gotoCarBrand(self, carbrand, carTitle):
        log.logger.info("Test_gotoCarBrand is started")
        home = HomePage(self.driver)
        home.gotoNewCars()
        car = BaseCarPage(self.driver)
        print(carbrand)
        if carbrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car Brand is : "+ title)
            assert title == carTitle , "Not on the correct page as Title is not matching"
        elif carbrand == "Bmw":
            home.gotoNewCars().selectBmw()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            assert title == carTitle, "Not on the correct page as Title is not matching"

        log.logger.info("*********** Moved to selected cars page successfully *********")

    @pytest.mark.skip
    @pytest.mark.parametrize("carbrand, carTitle", dataReader.get_data("carbrandtest"))
    def test_getCarNameAndPrice(self, carbrand, carTitle):
        log.logger.info("test_getCarNameAndPrice test is started")
        home = HomePage(self.driver)
        home.gotoNewCars()
        car = BaseCarPage(self.driver)
        print(carbrand)
        if carbrand == "Honda":
            home.gotoNewCars().selectHonda()
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), name="doHonda", attachment_type=AttachmentType.PNG)
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Bmw":
            home.gotoNewCars().selectBmw()
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), name="doBmw", attachment_type=AttachmentType.PNG)
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), name="doHyundai", attachment_type=AttachmentType.PNG)
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Toyota":
            home.gotoNewCars().selectToyota()
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), name="doToyota", attachment_type=AttachmentType.PNG)
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"

        log.logger.info("*********** test_getCarNameAndPrice test is  successfully finished *********")