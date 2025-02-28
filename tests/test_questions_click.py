import pytest
from locators.home_page_locators import Locators
from pages.home_page import HomePageMesto
import allure


class TestClickQuestions:

    @pytest.mark.parametrize("question_number, locator",[(1, Locators.question_1),(2, Locators.question_2),(3, Locators.question_3),(4, Locators.question_4),(5, Locators.question_5),(6, Locators.question_6),(7, Locators.question_7),(8, Locators.question_8),],)
    @allure.title("Проверка раскрытия вопроса №{question_number}")
    def test_question_expands_correctly(self,browser, question_number, locator):
        page = HomePageMesto(browser)
        page.wait_for_load_questions()
        page.scroll_to_element(locator)
        page.click_element(locator)
        question = page.find_element(locator)
        open_question = question.get_attribute('aria-disabled')
        assert open_question == 'true'