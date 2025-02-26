import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
import allure


class TestClickQuestions:

    @allure.title("Проверка раскрытия первого вопроса")
    def test_question_1_expands_correctly(self,browser):
        first_question = HomePageMesto(browser)
        first_question.wait_for_load_questions()
        first_question.scroll_to_element(Locators.question_1)
        first_question.click_element(Locators.question_1)
        first = first_question.find_element(Locators.question_1)
        open_first = first.get_attribute('aria-disabled')
        assert open_first == 'true'

    @allure.title("Проверка раскрытия второго вопроса")
    def test_question_2_expands_correctly(self,browser):
        second_question = HomePageMesto(browser)
        second_question.wait_for_load_questions()
        second_question.scroll_to_element(Locators.question_2)
        second_question.click_element(Locators.question_2)
        second = second_question.find_element(Locators.question_2)
        open_second = second.get_attribute('aria-disabled')
        assert open_second == 'true'

    @allure.title("Проверка раскрытия третьего вопроса")
    def test_question_3_expands_correctly(self,browser):
        third_question = HomePageMesto(browser)
        third_question.wait_for_load_questions()
        third_question.scroll_to_element(Locators.question_3)
        third_question.click_element(Locators.question_3)
        third = third_question.find_element(Locators.question_3)
        open_third = third.get_attribute('aria-disabled')
        assert open_third == 'true'

    @allure.title("Проверка раскрытия четвертого вопроса")
    def test_question_4_expands_correctly(self,browser):
        fourth_question = HomePageMesto(browser)
        fourth_question.wait_for_load_questions()
        fourth_question.scroll_to_element(Locators.question_4)
        fourth_question.click_element(Locators.question_4)
        fourth = fourth_question.find_element(Locators.question_4)
        open_fourth = fourth.get_attribute('aria-disabled')
        assert open_fourth == 'true'

    @allure.title("Проверка раскрытия пятого вопроса")
    def test_question_5_expands_correctly(self,browser):
        fifth_question = HomePageMesto(browser)
        fifth_question.wait_for_load_questions()
        fifth_question.scroll_to_element(Locators.question_5)
        fifth_question.click_element(Locators.question_5)
        fifth = fifth_question.find_element(Locators.question_5)
        open_fifth = fifth.get_attribute('aria-disabled')
        assert open_fifth == 'true'

    @allure.title("Проверка раскрытия шестого вопроса")
    def test_question_6_expands_correctly(self,browser):
        sixth_question = HomePageMesto(browser)
        sixth_question.wait_for_load_questions()
        sixth_question.scroll_to_element(Locators.question_6)
        sixth_question.click_element(Locators.question_6)
        sixth = sixth_question.find_element(Locators.question_6)
        open_sixth = sixth.get_attribute('aria-disabled')
        assert open_sixth == 'true'

    @allure.title("Проверка раскрытия седьмого вопроса")
    def test_question_7_expands_correctly(self, browser):
        seventh_question = HomePageMesto(browser)
        seventh_question.wait_for_load_questions()
        seventh_question.scroll_to_element(Locators.question_7)
        seventh_question.click_element(Locators.question_7)
        seventh = seventh_question.find_element(Locators.question_7)
        open_seventh = seventh.get_attribute('aria-disabled')
        assert open_seventh == 'true'

    @allure.title("Проверка раскрытия восьмого вопроса")
    def test_question_8_expands_correctly(self, browser):
        eight_question = HomePageMesto(browser)
        eight_question.wait_for_load_questions()
        eight_question.scroll_to_element(Locators.question_8)
        eight_question.click_element(Locators.question_8)
        eight = eight_question.find_element(Locators.question_8)
        open_eight = eight.get_attribute('aria-disabled')
        assert open_eight == 'true'