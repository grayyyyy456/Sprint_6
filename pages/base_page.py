from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)