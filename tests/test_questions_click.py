import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto


class TestClickQuestions:

    def test_question_1_expands_correctly(self,browser):
        first_question = HomePageMesto(browser)
        first_question.wait_for_load_questions()
        first_button = browser.find_element(*Locators.question_1)
        browser.execute_script("arguments[0].scrollIntoView(true);", first_button)
        first_question.click_first_question()
        first = browser.find_element(*Locators.question_1)
        open_first = first.get_attribute('aria-disabled')
        assert open_first == 'true'

    def test_question_2_expands_correctly(self,browser):
        second_question = HomePageMesto(browser)
        second_question.wait_for_load_questions()
        second_button = browser.find_element(*Locators.question_2)
        browser.execute_script("arguments[0].scrollIntoView(true);", second_button)
        second_question.click_second_question()
        second = browser.find_element(*Locators.question_2)
        open_second = second.get_attribute('aria-disabled')
        assert open_second == 'true'

    def test_question_3_expands_correctly(self,browser):
        third_question = HomePageMesto(browser)
        third_question.wait_for_load_questions()
        third_button = browser.find_element(*Locators.question_3)
        browser.execute_script("arguments[0].scrollIntoView(true);", third_button)
        third_question.click_third_question()
        third = browser.find_element(*Locators.question_3)
        open_third = third.get_attribute('aria-disabled')
        assert open_third == 'true'

    def test_question_4_expands_correctly(self,browser):
        fourth_question = HomePageMesto(browser)
        fourth_question.wait_for_load_questions()
        fourth_button = browser.find_element(*Locators.question_4)
        browser.execute_script("arguments[0].scrollIntoView(true);", fourth_button)
        fourth_question.click_fourth_question()
        fourth = browser.find_element(*Locators.question_4)
        open_fourth = fourth.get_attribute('aria-disabled')
        assert open_fourth == 'true'

    def test_question_5_expands_correctly(self,browser):
        fifth_question = HomePageMesto(browser)
        fifth_question.wait_for_load_questions()
        fifth_button = browser.find_element(*Locators.question_5)
        browser.execute_script("arguments[0].scrollIntoView(true);", fifth_button)
        fifth_question.click_fifth_question()
        fifth = browser.find_element(*Locators.question_5)
        open_fifth = fifth.get_attribute('aria-disabled')
        assert open_fifth == 'true'

    def test_question_6_expands_correctly(self,browser):
        sixth_question = HomePageMesto(browser)
        sixth_question.wait_for_load_questions()
        sixth_button = browser.find_element(*Locators.question_6)
        browser.execute_script("arguments[0].scrollIntoView(true);", sixth_button)
        sixth_question.click_sixth_question()
        sixth = browser.find_element(*Locators.question_6)
        open_sixth = sixth.get_attribute('aria-disabled')
        assert open_sixth == 'true'

    def test_question_7_expands_correctly(self, browser):
        seventh_question = HomePageMesto(browser)
        seventh_question.wait_for_load_questions()
        seventh_button = browser.find_element(*Locators.question_7)
        browser.execute_script("arguments[0].scrollIntoView(true);", seventh_button)
        seventh_question.click_seventh_question()
        seventh = browser.find_element(*Locators.question_7)
        open_seventh = seventh.get_attribute('aria-disabled')
        assert open_seventh == 'true'

    def test_question_8_expands_correctly(self, browser):
        eight_question = HomePageMesto(browser)
        eight_question.wait_for_load_questions()
        eight_button = browser.find_element(*Locators.question_8)
        browser.execute_script("arguments[0].scrollIntoView(true);", eight_button)
        eight_question.click_eight_question()
        eight = browser.find_element(*Locators.question_8)
        open_eight = eight.get_attribute('aria-disabled')
        assert open_eight == 'true'