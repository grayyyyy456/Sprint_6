from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_2_page_locators import Locators


class OrderPage2Mesto:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_form(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.field))

    def set_date_field(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_date))
        self.driver.find_element(*Locators.field_date).click()
        self.driver.find_element(*Locators.date_selection).click()

    def set_rental_period_field(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_rental_period))
        self.driver.find_element(*Locators.field_rental_period).click()
        self.driver.find_element(*Locators.rental_period_1).click()

    def set_color_field(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_color))
        self.driver.find_element(*Locators.black_color).click()

    def set_comment_field(self, comment):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.field_comment))
        self.driver.find_element(*Locators.field_comment).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        self.driver.find_element(*Locators.order_button).click()

    def set_page_2(self, comment):
        self.set_date_field()
        self.set_rental_period_field()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()


