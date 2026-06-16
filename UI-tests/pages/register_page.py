import allure
from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators

class RegisterPage(BasePage):

    @allure.step("Создать нового пользователя")
    def create_account(self, name, email, password):
        self.fill_input(RegisterPageLocators.NAME_INPUT, name)
        self.fill_input(RegisterPageLocators.EMAIL_INPUT, email)
        self.fill_input(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Получить текст ошибки пароля")
    def get_password_error(self):
        return self.get_text(
            RegisterPageLocators.PASSWORD_ERROR_TEXT
        )
    
    @allure.step("Перейти на страницу логина")
    def open_login_page(self):
        self.click(RegisterPageLocators.LOGIN_LINK)
