from selenium.webdriver.common.by import By


class Locators:
    yandex_button = (By.XPATH, './/div/a[@href="//yandex.ru"]')  # Кнопка 'Яндекс' в логитипе на главной странице
    scooter_button = (By.XPATH, './/div/a[@href="/"]')  # Кнопка 'самокат' в логотипе на главной странице
    order_button_up = (By.CLASS_NAME, 'Button_Button__ra12g')  #  Кнопка 'Заказать' сверху на домашней странице
    order_button_down = (By.CLASS_NAME, 'Home_FinishButton__1_cWm')  # Кнопка 'Заказать' снизу на домашней странице

    # 'Вопросы о важном' в конце страницы
    questions = (By.CLASS_NAME, 'Home_FAQ__3uVm4')  # Поле 'Вопросы о важном'
    question_1 = (By.ID,'accordion__heading-0')  # 1 вопрос закрытый
    question_2 = (By.ID,'accordion__heading-1')  # 2 вопрос закрытый
    question_3 = (By.ID, 'accordion__heading-2')  # 3 вопрос закрытый
    question_4 = (By.ID, 'accordion__heading-3')  # 4 вопрос закрытый
    question_5 = (By.ID, 'accordion__heading-4')  # 5 вопрос закрытый
    question_6 = (By.ID, 'accordion__heading-5')  # 6 вопрос закрытый
    question_7 = (By.ID, 'accordion__heading-6')  # 7 вопрос закрытый
    question_8 = (By.ID, 'accordion__heading-7')  # 8 вопрос закрытый
    question_open = (By.CSS_SELECTOR, '[aria-disabled="true"]')  # любой вопрос открытый

    confirmation_window_1 = (By.CLASS_NAME, 'Order_Modal__YZ-d3')  # Окно подтверждения заказа
    confirmation_window_2 = (By.CLASS_NAME, 'Order_Modal__YZ-d3')  # Окно, что заказ успешно создан
    order_button = (By.XPATH, './/button[text()="Заказать"]')  # Кнопка 'Заказать' на второй странице заказа
    yes_button = (By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and text()='Да']")  # Кнопка 'Да' для подтверждения заказа

    status_button = (By.XPATH, './/button[contains(@class, "Button_Button__ra12g") and text()="Посмотреть статус"]')  # Кнопка 'Посмотреть статус'



