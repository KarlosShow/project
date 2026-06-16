import allure
from pages.register_page import RegisterPage
from data.urls import REGISTER_PAGE_URL
from locators.login_page_locators import LoginPageLocators

@allure.feature('Registration')
class TestUserRegistration:

    @allure.title('User can open login page from registration form')
    def test_open_login_page_from_register(
        self,
        driver
    ):
        register_page = RegisterPage(driver)
        register_page.open(REGISTER_PAGE_URL)
        register_page.open_login_page()
        assert register_page.element_is_displayed(
            LoginPageLocators.LOGIN_BUTTON
        )

    @allure.title('Password validation error is displayed')
    def test_invalid_password_error(
        self,
        driver
    ):
        register_page = RegisterPage(driver)
        register_page.open(REGISTER_PAGE_URL)
        register_page.create_account(
            'TestUser',
            'test@test.ru',
            '123'
        )
        assert 'Некорректный пароль' in \
               register_page.get_password_error()
