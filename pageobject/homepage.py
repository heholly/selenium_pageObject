import time
from selenium.webdriver.support.ui import Select
from base.base import BasePage

elementsDict = {
    "homeLabel":"id=nav-logo",
    "searchType": "css selector=#nav-search select",
    "searchInput": "id=twotabsearchtextbox",
    "searchBtn": "xpath=//input[@type='submit']",
    "resultLabel": "css selector=span.a-color-state.a-text-bold"
}


class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_homepage(self, url):
        try:
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self.driver.get(url)
            self.wait_locate(10, elementsDict, "homeLabel")
            print(f"Success: Open homepage: {url}")
        except Exception as e:
            self.driver.quit()
            raise

    def search_product(self, searchType, searchInput):
        try:
            dropdown = Select(self.locate(elementsDict, "searchType"))
            dropdown.select_by_visible_text(searchType)
            time.sleep(1)
            self.locate(elementsDict, "searchInput").send_keys(searchInput)
            self.locate(elementsDict, "searchBtn").click()
            self.wait_locate(10, elementsDict, "resultLabel")
            print(f"Success: search {searchInput} under searchtype:{searchType}")
        except Exception as e:
            self.driver.quit()
            raise


