from pages.base_page import BasePage
from locators.home_page_locators import Locators
import allure



class HomePageMesto(BasePage):
    @allure.step("Ожидание загрузки вопросов")
    def wait_for_load_questions(self):
        self.wait_for_element(Locators.questions, timeout=5)

    @allure.step("Кликаем по первому вопросу")
    def click_first_question(self):
        self.click_element(Locators.question_1)

    @allure.step("Кликаем по второму вопросу")
    def click_second_question(self):
        self.click_element(Locators.question_2)

    @allure.step("Кликаем по третьему вопросу")
    def click_third_question(self):
        self.click_element(Locators.question_3)

    @allure.step("Кликаем по четвёртому вопросу")
    def click_fourth_question(self):
        self.click_element(Locators.question_4)

    @allure.step("Кликаем по пятому вопросу")
    def click_fifth_question(self):
        self.click_element(Locators.question_5)

    @allure.step("Кликаем по шестому вопросу")
    def click_sixth_question(self):
        self.click_element(Locators.question_6)

    @allure.step("Кликаем по седьмому вопросу")
    def click_seventh_question(self):
        self.click_element(Locators.question_7)

    @allure.step("Кликаем по восьмому вопросу")
    def click_eight_question(self):
        self.click_element(Locators.question_8)

    @allure.step("Кликаем по верхней кнопке заказа")
    def click_order_button_up(self):
        self.click_element(Locators.order_button_up)

    @allure.step("Кликаем по нижней кнопке заказа")
    def click_order_button_down(self):
        self.click_element(Locators.order_button_down)

    @allure.step("Кликаем на кнопку Самокат в лого")
    def click_scooter_logo(self):
        self.click_element(Locators.scooter_button)

    @allure.step("Кликаем на кнопку Яндекс в лого")
    def click_yandex_button(self):
        self.click_element(Locators.yandex_button)

    @allure.step("Переключение на последнюю открытую вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])



