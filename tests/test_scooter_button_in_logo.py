import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
from urls import url_scooter
import allure


class TestClickScooterButton:

    @allure.title("Проверка клика по логотипу Самоката")
    def test_click_scooter_button_in_logo(self, browser):
        logo_scooter_button = HomePageMesto(browser)
        logo_scooter_button.wait_for_load_questions()
        logo_scooter_button.click_order_button_up()
        logo_scooter_button.click_scooter_logo()
        assert browser.current_url == url_scooter