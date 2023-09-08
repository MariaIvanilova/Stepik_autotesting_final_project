from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert len(self.browser.find_elements(*ProductPageLocators.ADD_BASKET)) > 0,\
            "Locator can't be found for ADD_BASKET"
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def checks_product_in_basket(self):
        notification1 = self.browser.find_element(*ProductPageLocators.TEXT_ADD_TO_BASKET).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert len(self.browser.find_elements(*ProductPageLocators.BOOK_NAME)) > 0, \
            "Locator can't be found for BOOK_NAME"
        assert book_name in notification1, "name of book is not in notification"

        notification2 = self.browser.find_element(*ProductPageLocators.TEXT_BASKET_COST).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert len(self.browser.find_elements(*ProductPageLocators.BOOK_PRICE)) > 0,\
            "Locator can't be found for BOOK_PRICE"
        assert price in notification2, "basket coast is not equal book price"
