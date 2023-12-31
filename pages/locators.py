from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEE_BASKET_BUTTON = (By.CLASS_NAME, "btn-group")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators:
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    TEXT_BOOK_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    TEXT_BASKET_COST = (By.CSS_SELECTOR, "div.alert:nth-of-type(3) .alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasketPageLocators:
    TEXT_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
