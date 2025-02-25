from locators.order_2_page_locators import Locators
import allure
from pages.base_page import BasePage

class OrderPage2Mesto(BasePage):

    @allure.step("Ожидание загрузки второй страницы формы заказа")
    def wait_for_load_form(self):
        self.wait_for_element(Locators.field, timeout=5)

    @allure.step("Выбираем дату заказа")
    def set_date_field(self):
        self.click_element(Locators.field_date)
        self.click_element(Locators.date_selection)

    @allure.step("Выбираем срок аренды")
    def set_rental_period_field(self):
        self.click_element(Locators.field_rental_period)
        self.click_element(Locators.rental_period_1)

    @allure.step("Выбираем цвет")
    def set_color_field(self):
        self.click_element(Locators.black_color)

    @allure.step("Вводим комментарий: {comment}")
    def set_comment_field(self, comment):
        self.wait_for_element(Locators.field_comment)
        self.find_element(Locators.field_comment).send_keys(comment)

    @allure.step("Кликаем на кнопку заказа")
    def click_order_button(self):
        self.click_element(Locators.order_button)

    @allure.step("Заполняем страницу 2 заказа")
    def set_page_2(self, comment):
        self.set_date_field()
        self.set_rental_period_field()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()


