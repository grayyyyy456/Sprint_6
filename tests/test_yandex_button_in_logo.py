import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
from conftest import browser


class TestClickScooterButton:

    def test_click_yandex_button_in_logo(self, browser):
        logo_yandex_button = HomePageMesto(browser)
        logo_yandex_button.wait_for_load_questions()
        browser.find_element(*Locators.yandex_button).click()
        browser.switch_to.window(browser.window_handles[-1])
        url_yandex = 'https://dzen.ru/?yredirect=true'
        WebDriverWait(browser, 10).until(expected_conditions.url_to_be(url_yandex))
        assert browser.current_url == url_yandex
