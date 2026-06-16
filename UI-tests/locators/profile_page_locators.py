from selenium.webdriver.common.by import By

class ProfilePageLocators:

    PROFILE_BUTTON = (By.XPATH,"//p[text()='Личный Кабинет']")
    PROFILE_HEADER = (By.XPATH,"//a[contains(text(),'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH,"//button[text()='Выход']")