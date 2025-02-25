import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
from urls import url_order
import allure



class TestClickOrderButtons:

    @allure.title("Проверка нажатия на верхнюю кнопку заказа")
    def test_click_1_order_button(self, browser):
        first_button = HomePageMesto(browser)
        first_button.wait_for_load_questions()
        first_button.click_element(Locators.order_button_up)
        assert browser.current_url == url_order

    @allure.title("Проверка нажатия на нижнюю кнопку заказа")
    def test_click_2_order_button(self, browser):
        second_button = HomePageMesto(browser)
        second_button.wait_for_load_questions()
        second_button.scroll_to_element(Locators.order_button_down)
        second_button.click_element(Locators.order_button_down)
        assert browser.current_url == url_order