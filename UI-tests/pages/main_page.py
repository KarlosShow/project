import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self, url):
        self.open(url)
    
    @allure.step("Открыть раздел Лента заказов")
    def open_feed_section(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains('/feed')
    
    @allure.step("Открыть раздел Конструктор")
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Открыть модальное окно ингредиента")
    def open_ingredient_modal(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_order(self):
        self.drag_element(
            MainPageLocators.FIRST_FILLING,
            MainPageLocators.BURGER_CONSTRUCTOR_AREA
        )

    @allure.step("Проверить отображение модального окна ингредиента")
    def ingredient_modal_visible(self):
        return self.element_is_displayed(
            MainPageLocators.INGREDIENT_MODAL
        )
    
    @allure.step("Проверить наличие ингредиента в конструкторе")
    def constructor_area_has_item(self):
        return self.element_is_displayed(
            MainPageLocators.CONSTRUCTOR_ITEM
        )
