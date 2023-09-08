from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    TEXT_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alert:nth-of-type(1)")
    TEXT_BASKET_COST = (By.CSS_SELECTOR, "div.alert:nth-of-type(3) .alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
