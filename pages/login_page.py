from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link_text = self.browser.current_url
        assert 'login' in link_text, 'url не содержит подстроку login'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert len(self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)), 'нет формы логина'
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert len(self.browser.find_elements(*LoginPageLocators.REGISTRATION_FORM)), 'нет формы регистрации'
        # assert True
