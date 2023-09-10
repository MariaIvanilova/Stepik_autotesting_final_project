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
        # assert len(self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)), 'нет формы логина'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is absent'
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert len(self.browser.find_elements(*LoginPageLocators.REGISTRATION_FORM)), 'нет формы регистрации'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is absent'
        # assert True

    def register_new_user(self, mail, password):
        email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email.send_keys(mail)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
