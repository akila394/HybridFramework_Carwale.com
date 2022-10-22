import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utilities import configReader
#from Utilities.configReader import readConfig
from selenium.webdriver.support.select import Select
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator)).click()
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("webelements", locator)).click()
        log.logger.info("Clicking on an element"+str(locator))


    def type(self,locator, value):
        if str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator)).send_keys(value)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("webelements", locator)).send_keys(value)
        log.logger.info("Typing in an element :  " + str(locator) + " with the value " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("webelements", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Select the  option " + str(value) + "for the " + str(locator))

    def moveTo(self,locator):
        global element
        if str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("webelements", locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element :  " + str(locator))

    def sliderDragAndDrop(self, locator, xvalue, yvalue):
        global element
        if str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("webelements", locator))
        log.logger.info("Clicking on an element"+str(locator))

        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, xvalue, yvalue).perform()

    def clickJavaScript(self, locator):
        global element
        if str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("webelements", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("webelements", locator))

        self.driver.execute_script("arguments[0].click();", element)

        log.logger.info("Clicking on an element"+str(locator))
