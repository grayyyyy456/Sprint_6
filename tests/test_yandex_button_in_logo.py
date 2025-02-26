import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.home_page import HomePageMesto
from urls import url_yandex
import allure


class TestClickScooterButton:

    @allure.title("Проверка клика по логотипу Яндекс")
    def test_click_yandex_button_in_logo(self, browser):
        logo_yandex_button = HomePageMesto(browser)
        logo_yandex_button.wait_for_load_questions()
        logo_yandex_button.click_yandex_button()
        logo_yandex_button.switch_to_last_tab()
        WebDriverWait(browser, 10).until(expected_conditions.url_to_be(url_yandex))
        assert logo_yandex_button.get_current_url() == url_yandex
