import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
from urls import url_order


class TestClickOrderButtons:

    def test_click_1_order_button(self, browser):
        first_button = HomePageMesto(browser)
        first_button.wait_for_load_questions()
        first_button_click = browser.find_element(*Locators.order_button_up)
        first_button_click.click()
        assert browser.current_url == url_order

    def test_click_2_order_button(self, browser):
        second_button = HomePageMesto(browser)
        second_button.wait_for_load_questions()
        second_button_click = browser.find_element(*Locators.order_button_down)
        browser.execute_script("arguments[0].scrollIntoView(true);", second_button_click)
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.order_button_down))
        second_button_click.click()
        assert browser.current_url == url_order