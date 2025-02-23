import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
from conftest import browser


class TestClickScooterButton:

    def test_click_scooter_button_in_logo(self, browser):
        logo_scooter_button = HomePageMesto(browser)
        logo_scooter_button.wait_for_load_questions()
        browser.find_element(*Locators.order_button_up).click()
        browser.find_element(*Locators.scooter_button).click()
        url_scooter = 'https://qa-scooter.praktikum-services.ru/'
        assert browser.current_url == url_scooter