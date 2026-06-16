import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.fill_input(LoginPageLocators.EMAIL_INPUT, email)
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Дождаться отображения формы логина")
    def wait_login_form(self):
        return self.element_is_displayed(
            LoginPageLocators.LOGIN_BUTTON
        )
