import pytest
from selenium.webdriver.common.by import By

from PageObjects.BaseCarPage import BaseCarPage
from PageObjects.HomePage import HomePage
from Tests.basetest import BaseTest
from Utilities import dataReader, configReader
from Utilities.LogUtil import Logger
import logging

log = Logger(__name__, logging.INFO)
class Test_searchAndFilter(BaseTest):

    @pytest.mark.parametrize("carbrand, carTitle", dataReader.get_data("filtercars"))
    def test_searchUsingBudget(self, carbrand, carTitle):
        log.logger.info("Test_gotoCarBrand is started")
        home = HomePage(self.driver)
        home.gotoNewCars()
        car = BaseCarPage(self.driver)
        print(carbrand)
        if carbrand == "Honda":
            home.gotoNewCars().selectHonda()
            car.filterCarsbyBudget()
            carpricelist = car.getCarPrice() #This returns all the  car prices given by search result
            pricerange = car.getPriceRange() # This returns the price range of the search results
            listofstates = []
            for i in range(0,len(carpricelist)):
                price = carpricelist[i].text
                value = price.split(" ")
                print(value[1])
                if float(pricerange[0]) < float(value[1]) < float(pricerange[1]):
                    listofstates.append("Pass")
                else:
                    listofstates.append(("Fail"))

            if "Fail" not in listofstates:
                log.logger.info("************** Search using Budget for Honda Passed *****************")
                assert True
            else:
                log.logger.info("************** Search using Budget for Honda Failed *****************")
                assert False

        elif carbrand == "Toyota":
            home.gotoNewCars().selectToyota()
            car.filterCarsbyBudget()
            carpricelist = car.getCarPrice()  # This returns all the  car prices given by search result
            pricerange = car.getPriceRange()  # This returns the price range of the search results
            listofstates = []
            for i in range(0, len(carpricelist)):
                price = carpricelist[i].text
                value = price.split(" ")
                print(value[1])
                if float(pricerange[0]) < float(value[1]) < float(pricerange[1]):
                    listofstates.append("Pass")
                else:
                    listofstates.append(("Fail"))

            if "Fail" not in listofstates:
                log.logger.info("************** Search using  Budget for Toyota Passed *****************")
                assert True
            else:
                log.logger.info("************** Search using Budget for Toyota Failed *****************")
                assert False
        elif carbrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            car.filterCarsbyBudget()
            carpricelist = car.getCarPrice()  # This returns all the  car prices given by search result
            pricerange = car.getPriceRange()  # This returns the price range of the search results
            listofstates = []
            for i in range(0, len(carpricelist)):
                price = carpricelist[i].text
                value = price.split(" ")
                print(value[1])
                if float(pricerange[0]) < float(value[1]) < float(pricerange[1]):
                    listofstates.append("Pass")
                else:
                    listofstates.append(("Fail"))

            if "Fail" not in listofstates:
                log.logger.info("************** Search using Budget for Hyundai Passed *****************")
                assert True
            else:
                log.logger.info("************** Search using Budget for Hyundai Failed *****************")
                assert False

        elif carbrand == "BMW":
            home.gotoNewCars().selectBmw()
            car.filterCarsbyBudget()
            carpricelist = car.getCarPrice()  # This returns all the  car prices given by search result
            pricerange = car.getPriceRange()  # This returns the price range of the search results
            listofstates = []
            for i in range(0, len(carpricelist)):
                price = carpricelist[i].text
                value = price.split(" ")
                print(value[1])
                if float(pricerange[0]) < float(value[1]) < float(pricerange[1]):
                    listofstates.append("Pass")
                else:
                    listofstates.append(("Fail"))

            if "Fail" not in listofstates:
                log.logger.info("************** Search using Budget for BMW Passed *****************")
                assert True
            else:
                log.logger.info("************** Search using Budget for BMW Failed *****************")
                assert False
