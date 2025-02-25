from pages.base_page import BasePage
from locators.home_page_locators import Locators



class HomePageMesto(BasePage):

    def wait_for_load_questions(self):
        self.wait_for_element(Locators.questions, timeout=5)

    def click_first_question(self):
        self.click_element(Locators.question_1)

    def click_second_question(self):
        self.click_element(Locators.question_2)

    def click_third_question(self):
        self.click_element(Locators.question_3)

    def click_fourth_question(self):
        self.click_element(Locators.question_4)

    def click_fifth_question(self):
        self.click_element(Locators.question_5)

    def click_sixth_question(self):
        self.click_element(Locators.question_6)

    def click_seventh_question(self):
        self.click_element(Locators.question_7)

    def click_eighth_question(self):
        self.click_element(Locators.question_8)



