from selenium.webdriver.common.by import By

class Locators:
    field_date = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')  # Поле заполнения даты, когда привезти
    date_selection = (By.XPATH, './/div[text()="30"]')  # Выбор определнной даты

    field_rental_period = (By.CLASS_NAME, 'Dropdown-placeholder')  # Поле заполнения срок аренды
    rental_period_1 = (By.XPATH, './/div[text()="сутки"]')  # Первое значение в выпадающий списке срока аренды
    rental_period_2 = (By.XPATH, './/div[text()="двое суток"]')  # Второе значение в выпадающий списке срока аренды

    field_color = (By.CLASS_NAME, 'Order_Checkboxes__3lWSI')  # Поле заполнения цвета
    black_color = (By.ID, 'black')  # Выбор черного цвета
    grey_color = (By.ID, 'grey')  # Выбор серого цвета

    field_comment = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')  # Поле заполнения комментария

    order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")  # Кнопка 'Заказать' на второй странице заказа

    yes_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']")  # Кнопка 'Да' для подтверждения заказа

    field = (By.ID, 'root')  # Страница(для загрузки ее целиком)
