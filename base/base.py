from selenium import webdriver
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def locate(self, object, object_value, elementNum=1):
        if object is None:
            locator = object_value.split("=", 1)
        else:
            locator = str(object[object_value]).split("=", 1)
        try:
            if elementNum == 1:
                el = self.driver.find_element(*locator)
                time.sleep(1)
                print(f"Success: Find the element with pathtype:{locator[0]} and pathvalue:{locator[1]}")
                return el
                # if el.is_displayed():
                #     print(f"The element pathtype:{locator[0]} and pathvalue:{locator[1]} is visible on page")
                #     return el
                # else:
                #     self.driver.quit()
                #     raise Exception(f"Failed: the element pathtype:{locator[0]} "
                #                     f"and pathvalue:{locator[1]} isn't visible")
            else:
                els = self.driver.find_elements(*locator)
                return els
        except Exception as e:
            self.driver.quit()
            raise Exception(f"Can not find element by pathtype:{locator[0]} and pathvalue:{locator[1]}")

    def wait_locate(self, waitTime, object, object_value):
        try:
            locator = str(object[object_value]).split("=", 1)
            WebDriverWait(self.driver, waitTime).until(EC.presence_of_element_located((locator[0], locator[1])))
        except Exception as e:
            self.driver.quit()
            raise
