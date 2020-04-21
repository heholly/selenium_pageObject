import os
import configparser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class EnvironmentSetup:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("config.ini")
        self.url = conf.get("amazon", "url")
        self.browser = conf.get("amazon", "browser").lower()
        self.time_out = int(conf.get("amazon", "time_out"))
        self.browser_path = conf.get("amazon", "browser_path")
        self.filename = conf.get("amazon", "filename")

    def initBrowser(self):
        try:
            if self.browser =="chrome":
                driver = webdriver.Chrome(executable_path=self.browser_path)
            elif self.browser == "firefox":
                driver = webdriver.firefoxe(executable_path=self.browser_path)
            elif self.browser == "ie":
                driver = webdriver.ie(executable_path=self.browser_path)
            else:
                print("browser type is out of scope")
                raise Exception
            return driver
        except Exception as e:
            raise


if __name__=='__main__':
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    # items = conf.items("amazon")
    url = conf.get("amazon", "url")
    print(url)
    browser = conf.get("amazon", "browser").lower()
    print(browser)
    time_out = int(conf.get("amazon", "time_out"))
    browser_path = conf.get("amazon", "browser_path")

