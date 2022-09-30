import configparser
from configparser import ConfigParser

def readConfig(section,key):
    config = ConfigParser()
    config.read("..\\ConfigurationFiles\\config.ini")
    return config.get(section,key)


