from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS, 5)

    def check_text_basket_empty(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_BASKET).text
        check_text = "Your basket is empty"
        assert check_text in text, f"correct test '{check_text}' is not present"
