from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    def open(self, url):
        self.driver.get(url)
    def wait_until_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    def wait_until_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
    def click(self, locator):
        self.wait_until_clickable(locator).click()
    def fill_input(self, locator, value):
        field = self.wait_until_visible(locator)
        field.clear()
        field.send_keys(value)
    def get_text(self, locator):
        return self.wait_until_visible(locator).text
    def element_is_displayed(self, locator):
        try:
            return self.wait_until_visible(locator).is_displayed()
        except Exception:
            return False
    def wait_for_url_contains(self, value):
        self.wait.until(
            EC.url_contains(value)
        )
    def drag_element(self, source_locator, target_locator):
        source = self.wait_until_visible(source_locator)
        target = self.wait_until_visible(target_locator)
        ActionChains(self.driver) \
            .drag_and_drop(source, target) \
            .perform()
    def element_is_not_visible(self, locator):
        try:
            return self.wait.until(
            EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
