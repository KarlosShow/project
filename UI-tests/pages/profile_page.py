import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):

    @allure.step("Открыть личный кабинет")
    def open_profile(self):
        self.click(ProfilePageLocators.PROFILE_BUTTON)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Дождаться загрузки страницы профиля")
    def wait_profile_page(self):
        return self.element_is_displayed(
            ProfilePageLocators.PROFILE_HEADER
        )
