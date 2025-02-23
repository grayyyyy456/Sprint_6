import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_1_page_locators import Locators


class OrderPage1Mesto:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_form(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.field))

    def set_name_field(self, name):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_name))
        self.driver.find_element(*Locators.field_name).send_keys(name)

    def set_last_name_field(self, last_name):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_last_name))
        self.driver.find_element(*Locators.field_last_name).send_keys(last_name)

    def set_address_field(self, address):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_address))
        self.driver.find_element(*Locators.field_address).send_keys(address)

    def set_metro_field(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_metro))
        self.driver.find_element(*Locators.field_metro).click()
        self.driver.find_element(*Locators.metro).click()

    def set_phone_field(self, phone):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_phone))
        self.driver.find_element(*Locators.field_phone).send_keys(phone)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.next_button))
        self.driver.find_element(*Locators.next_button).click()

    def set_page_1(self, name, last_name, address, metro, phone):
        self.set_name_field(name)
        self.set_last_name_field(last_name)
        self.set_address_field(address)
        self.set_metro_field()
        self.set_phone_field(phone)
        self.click_next_button()


