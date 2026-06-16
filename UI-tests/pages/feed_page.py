import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    @allure.step("Открыть детали первого заказа")
    def open_order_details(self):
        self.click(FeedPageLocators.FIRST_ORDER)

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        self.click(FeedPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_feed_loaded(self):
        return self.element_is_displayed(
            FeedPageLocators.ORDER_FEED_TITLE
        )
    
    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text(
            FeedPageLocators.ORDER_NUMBER
        )
