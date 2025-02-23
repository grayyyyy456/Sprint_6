from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import Locators


class HomePageMesto:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_load_questions(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.questions))

    def click_first_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_1))
        first_button = self.driver.find_element(*Locators.question_1)
        first_button.click()

    def click_second_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_2))
        second_button = self.driver.find_element(*Locators.question_2)
        second_button.click()


    def click_third_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_3))
        third_button = self.driver.find_element(*Locators.question_3)
        third_button.click()


    def click_fourth_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_4))
        fourth_button = self.driver.find_element(*Locators.question_4)
        fourth_button.click()

    def click_fifth_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_5))
        fifth_button = self.driver.find_element(*Locators.question_5)
        fifth_button.click()


    def click_sixth_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_6))
        sixth_button = self.driver.find_element(*Locators.question_6)
        sixth_button.click()


    def click_seventh_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_7))
        seventh_button = self.driver.find_element(*Locators.question_7)
        seventh_button.click()


    def click_eight_question(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.question_8))
        eight_button = self.driver.find_element(*Locators.question_8)
        eight_button.click()



