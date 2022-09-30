import time

import pytest

from PageObjects.BaseCarPage import BaseCarPage
from PageObjects.HomePage import HomePage
from Tests.basetest import BaseTest
from Utilities import dataReader
from Utilities.LogUtil import Logger
import logging

log = Logger(__name__, logging.INFO)
class Test_CarWale(BaseTest):
    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("*********** Inside the New car Test ************")
        home = HomePage(self.driver)
        home.gotoNewCars()
        log.logger.info("*********** Moved to new cars page successfully *********")
        time.sleep(5)

    @pytest.mark.skip
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


    @pytest.mark.parametrize("carbrand, carTitle", dataReader.get_data("carbrandtest"))
    def test_getCarNameAndPrice(self, carbrand, carTitle):
        log.logger.info("test_getCarNameAndPrice test is started")
        home = HomePage(self.driver)
        home.gotoNewCars()
        car = BaseCarPage(self.driver)
        print(carbrand)
        if carbrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Bmw":
            home.gotoNewCars().selectBmw()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"
        elif carbrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car Brand is : " + title)
            print(car.getCarPriceAndName())
            assert title == carTitle, "Not on the correct page as Title is not matching"

        log.logger.info("*********** test_getCarNameAndPrice test is  successfully finished *********")