from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH,"//fieldset[1]//input")
    EMAIL_INPUT = (By.XPATH,"//fieldset[2]//input")
    PASSWORD_INPUT = (By.XPATH,"//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH,"//a[text()='Войти']")
    PASSWORD_ERROR_TEXT = (By.XPATH,"//*[contains(text(),'Некорректный пароль')]")