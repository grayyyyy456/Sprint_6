from locators.order_1_page_locators import Locators
import allure
from pages.base_page import BasePage
from pages.home_page import HomePageMesto

class OrderPage1Mesto(HomePageMesto, BasePage):

    @allure.step("Ожидаем загрузку формы")
    def wait_for_load_form(self):
        self.wait_for_element(Locators.field)

    @allure.step("Заполняем поле 'Имя': {name}")
    def set_name_field(self, name):
        self.wait_for_element(Locators.field_name, timeout=10)
        self.find_element(Locators.field_name).send_keys(name)

    @allure.step("Заполняем поле 'Фамилия': {last_name}")
    def set_last_name_field(self, last_name):
        self.wait_for_element(Locators.field_last_name, timeout=10)
        self.find_element(Locators.field_last_name).send_keys(last_name)

    @allure.step("Заполняем поле 'Адрес': {address}")
    def set_address_field(self, address):
        self.wait_for_element(Locators.field_address, timeout=10)
        self.find_element(Locators.field_address).send_keys(address)

    @allure.step("Выбираем станцию метро")
    def set_metro_field(self):
        self.wait_for_element(Locators.field_metro, timeout=10)
        self.find_element(Locators.field_metro).click()
        self.find_element(Locators.metro).click()

    @allure.step("Заполняем поле 'Телефон': {phone}")
    def set_phone_field(self, phone):
        self.wait_for_element(Locators.field_phone, timeout=10)
        self.find_element(Locators.field_phone).send_keys(phone)

    @allure.step("Нажимаем кнопку 'Далее'")
    def click_next_button(self):
        self.wait_for_element(Locators.next_button, timeout=10)
        self.find_element(Locators.next_button).click()

    @allure.step("Заполняем страницу 1 формы: {name}, {last_name}, {address}, {metro}, {phone}")
    def set_page_1(self, name, last_name, address, metro, phone):
        self.set_name_field(name)
        self.set_last_name_field(last_name)
        self.set_address_field(address)
        self.set_metro_field()
        self.set_phone_field(phone)
        self.click_next_button()


