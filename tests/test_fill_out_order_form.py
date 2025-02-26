import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import Locators
from pages.order_1_page import OrderPage1Mesto
from pages.order_2_page import OrderPage2Mesto
import allure


class TestFillOutOrderForm:

    @allure.title("Проверка заполнения формы заказа")
    @pytest.mark.parametrize("name, last_name, address, metro, phone, comment", [
        ("Иван", "Иванов", "Усачева 3", "Сокольники", "12312312311", "zakaz1"),
        ("Петр", "Петров", "Белорусская 16", "Лубянка", "98765498765", "zakaz2"),])
    def test_fill_out_order_form(self, browser, name, last_name, address, metro, phone, comment):
        order = OrderPage1Mesto(browser)
        order.wait_for_load_form()
        order.click_order_button_up()
        order.set_page_1(name, last_name, address, metro, phone)
        order_page_2 = OrderPage2Mesto(browser)
        order_page_2.wait_for_load_form()
        order_page_2.set_page_2(comment)
        order_page_2.wait_for_element(Locators.confirmation_window_1)
        order_page_2.click_element(Locators.yes_button)
        window = order_page_2.find_element(Locators.status_button)
        assert window.is_displayed()




