from selenium.webdriver.common.by import By

class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH,"//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH,"//p[text()='Лента Заказов']")
    FIRST_INGREDIENT = (By.XPATH,"(//a[contains(@class,'BurgerIngredient_ingredient')])[1]")
    CLOSE_MODAL_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_MODAL = (By.XPATH,"//h2[text()='Детали ингредиента']")
    FIRST_FILLING = (By.XPATH,"(//a[contains(@class,'BurgerIngredient_ingredient')])[2]")
    BURGER_CONSTRUCTOR_AREA = (By.XPATH,"//section[contains(@class,'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEM = (By.XPATH,"//section[contains(@class,'BurgerConstructor_basket')]//li")
    ORDER_COUNTER = (By.XPATH,"(//*[contains(@class,'counter_counter__num')])[1]")