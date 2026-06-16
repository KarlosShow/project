from selenium.webdriver.common.by import By

class FeedPageLocators:

    ORDER_FEED_TITLE = (By.XPATH,"//h1[contains(text(),'Лента заказов')]")
    FIRST_ORDER = (By.XPATH,"(//li[contains(@class,'OrderHistory_listItem')])[1]")
    CLOSE_MODAL_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH,"//p[contains(@class,'text_type_digits-large')]")
    TOTAL_COUNTER = (By.XPATH,"(//*[contains(@class,'OrderFeed_number')])[1]")