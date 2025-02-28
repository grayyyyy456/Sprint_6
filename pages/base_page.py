from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from locators.home_page_locators import Locators

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

    @allure.step("Переключение на последнюю открытую вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ждем загрузку страницы")
    def wait_load_page(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Клик по кнопке заказа")
    def click_order_button(self):
        element = self.wait_for_element(Locators.order_button_up)
        element.click()

    @allure.step("Скролим до нижней кнопки Заказать")
    def scroll_to_order_button_down(self):
        element = self.wait_for_element(Locators.order_button_down)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидание загрузки окна подтверждения")
    def wait_for_confirmation_window(self, timeout=10):
        return self.wait.until(expected_conditions.visibility_of_element_located(Locators.confirmation_window_1))

    @allure.step("Клик по кнопке 'Да' в окне подтверждения")
    def click_yes_button(self):
        element = self.wait_for_element(Locators.yes_button)
        element.click()

    @allure.step("Ищем кнопку 'Посмотреть статус'")
    def find_status_button(self):
        return self.driver.find_element(*Locators.status_button)

