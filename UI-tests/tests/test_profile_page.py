import allure
from data.urls import LOGIN_PAGE_URL
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

@allure.feature('User profile')
class TestProfilePage:

    @allure.title('Authorized user can logout')
    def test_logout(
        self,
        driver,
        authorized_user
    ):
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        profile_page.open(LOGIN_PAGE_URL)
        login_page.login(
            authorized_user['credentials']['email'],
            authorized_user['credentials']['password']
        )
        profile_page.open_profile()
        profile_page.logout()
        assert login_page.wait_login_form()