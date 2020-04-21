import unittest
from environmentSetup.environmentSetup import EnvironmentSetup
from pageobject.homepage import Homepage
from pageobject.searchResultPage import SearchResultPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        environ = EnvironmentSetup()
        self.driver = environ.initBrowser()
        self.url = environ.url
        self.time_out = environ.time_out
        self.filename = environ.filename

    def tearDown(self):
        self.driver.quit()

    def test_extract_search_data(self):
        try:
            homepage = Homepage(self.driver)
            homepage.open_homepage(self.url)
            homepage.search_product("Electronics", "kindle")
            searchpage = SearchResultPage(self.driver)
            result = searchpage.save_dict_to_text(self.filename)
            self.assertTrue(result)
        except Exception as e:
            raise


if __name__ == '__main__':
    unittest.main()
