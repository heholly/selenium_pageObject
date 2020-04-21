import json
from selenium.common.exceptions import NoSuchElementException
from base.base import BasePage
elementsDict = {
    "productItems": "css selector=[class='s-result-list s-search-results sg-row']>div[data-index]",
    "productName": "h2>a>span",
    "productPrice_1": "span[class='a-price']",
    "productPrice_2": "span[class='a-color-base']"
}
# fileName = "productList.txt"


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def extract_data_to_dict(self):
        try:
            productsList = []
            eles = self.locate(elementsDict, "productItems", elementNum=2)
            for element in eles:
                productName = " "
                productPrice = " "
                el = element.find_element_by_css_selector(elementsDict["productName"])
                productName = el.text
                try:
                    productPrice = element.find_element_by_css_selector(elementsDict["productPrice_1"]).text
                    priceStr = str(productPrice).split("\n", 1)
                    productPrice = priceStr[0] + "." + priceStr[1]
                except NoSuchElementException:
                    try:
                        productPrice = element.find_element_by_xpath(elementsDict["productPrice_2"]).text
                    except NoSuchElementException:
                        productPrice = "Null"

                productDict = {"Product_id": element.get_attribute("data-index"),
                               "Product_name": productName, "Product_price": productPrice}
                productsList.append(productDict)
                print(productDict)
            print("Success: Save the search data as a list of dictionary")
            return productsList
        except Exception as e:
            self.driver.quit()
            raise

    def save_dict_to_text(self, fileName):
        try:
            fileTxt = open(fileName, "w", encoding='utf-8')
            productsList = self.extract_data_to_dict()
            json.dump(productsList, fileTxt)
            fileTxt.close()
            print("Success: Save the list of dictionary into a TXT file")
            return True
        except Exception as e:
            raise
