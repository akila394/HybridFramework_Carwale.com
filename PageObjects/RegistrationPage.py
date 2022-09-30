import time
from PageObjects.BasePage import BasePage


class Registration(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def fillForm(self,name, phone_no, email,country, city, username, password):
        self.type("name_XPATH", name)
        self.type("phone_XPATH",phone_no)
        self.type("email_XPATH",email)
        self.select("country_XPATH",country)
        self.type("city_XPATH", city)
        self.type("username_XPATH", username)
        self.type("password_XPATH", password)
        time.sleep(5)
        self.click("submit_XPATH")
