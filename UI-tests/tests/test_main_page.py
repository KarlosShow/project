import allure
from data.urls import BASE_URL
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.feature('Constructor')
class TestBurgerConstructor:

    @allure.title('Ingredient modal window opens correctly')
    def test_open_ingredient_modal(
        self,
        driver
    ):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.open_ingredient_modal()
        assert main_page.ingredient_modal_visible()

    @allure.title('Ingredient modal can be closed')
    def test_close_ingredient_modal(
        self,
        driver
    ):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.open_ingredient_modal()
        main_page.close_ingredient_modal()
        assert main_page.element_is_not_visible(
            MainPageLocators.INGREDIENT_MODAL
)

    @allure.title('Ingredient can be added into constructor')
    def test_add_ingredient_to_constructor(
        self,
        driver
    ):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.add_ingredient_to_order()
        assert main_page.constructor_area_has_item()