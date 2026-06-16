import allure
from data.urls import BASE_URL
from pages.main_page import MainPage
from pages.feed_page import FeedPage

@allure.feature('Order feed')
class TestOrderFeed:

    @allure.title('User can open order feed section')
    def test_open_feed_page(
        self,
        driver
    ):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open(BASE_URL)
        main_page.open_feed_section()
        assert feed_page.wait_feed_loaded()

    @allure.title('Order details modal opens from feed')
    def test_open_order_details(
        self,
        driver
    ):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open(BASE_URL)
        main_page.open_feed_section()
        feed_page.open_order_details()
        assert feed_page.get_order_number() != ''