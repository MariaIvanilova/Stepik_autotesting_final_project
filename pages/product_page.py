from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Locator can't be found for ADD_BASKET"
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def checks_product_in_basket(self):
        notification1 = self.browser.find_element(*ProductPageLocators.TEXT_BOOK_ADD_TO_BASKET).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Locator can't be found for BOOK_NAME"
        assert book_name == notification1, "Name of book is not in notification"

        notification2 = self.browser.find_element(*ProductPageLocators.TEXT_BASKET_COST).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Locator can't be found for BOOK_PRICE"
        assert price in notification2, "Basket coast is not equal book price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
