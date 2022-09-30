import pytest
from PageObjects.RegistrationPage import Registration
from Tests.basetest import BaseTest
from Utilities import dataReader
from Utilities.LogUtil import Logger
import logging

log = Logger(__name__, logging.INFO)
class Test_Signup_001(BaseTest):

    @pytest.mark.parametrize("name,phone_no, email,country, city, username, password", dataReader.get_data("logintest"))
    def test_Signup_001(self,name,phone_no,email,country, city, username, password):

        log.logger.info("Test_signup_001 is started")

        regpage = Registration(self.driver)
        regpage.fillForm(name, phone_no, email, country, city, username, password)
        log.logger.info("Test_signup_001 is finished")