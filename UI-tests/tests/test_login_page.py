import allure
from data.urls import LOGIN_PAGE_URL
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.profile_page_locators import ProfilePageLocators

@allure.feature('Authorization')
class TestUserAuthorization:

    @allure.title('Existing user can login into account')
    def test_registered_user_can_login(
        self,
        driver,
        authorized_user
    ):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        main_page.open(LOGIN_PAGE_URL)
        login_page.login(
            authorized_user['credentials']['email'],
            authorized_user['credentials']['password']
        )
        assert main_page.element_is_displayed(
            ProfilePageLocators.PROFILE_BUTTON
        )
