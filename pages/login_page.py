from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
       self.should_be_login_url()
       self.should_be_login_form()
       self.should_be_register_form()
       
       # Три проверки что есть login_url, login_form, register_form

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "'login' not in current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login register form is not presented"
        
        
        
    def register_new_user(self, email, password):
        # Метод регистрирует нового пользователя
        
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_pass.send_keys(password)
        
        confirm_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_pass.send_keys(password)
        
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
        