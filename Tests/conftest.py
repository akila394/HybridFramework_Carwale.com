import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Utilities import configReader


@pytest.fixture(params=["chrome"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        ser = Service("C:\\Users\\dissanayake\\Desktop\\PythonSelenium\\drivers\\chromedriver.exe")
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)
    elif request.param == "firefox":
        ser = Service("C:\\Users\\dissanayake\\Desktop\\PythonSelenium\\drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=ser)
    elif request.param == "edge":
        ser = Service("C:\\Users\\dissanayake\\Desktop\\PythonSelenium\\drivers\\msedgedriver.exe")
        driver = webdriver.Edge(service=ser)
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.get(configReader.readConfig('basicinfo', 'testsiteURL2'))
    driver.maximize_window()

    yield driver
    driver.quit()
