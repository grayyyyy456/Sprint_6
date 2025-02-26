from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание загрузки элемента")
    def wait_for_element(self, locator, timeout=10):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Кликаем на элемент")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ищем элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Скролим до нужного элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получаем url на котором находимся")
    def get_current_url(self):
        return self.driver.current_url