from selenium.webdriver.common.by import By

class Locators:
    field_name = (By.CSS_SELECTOR, '[placeholder="* Имя"]')  # Поле заполнения имени
    field_last_name = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')  # Поле заполнения фамилии
    field_address = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')  # Поле заполнения адреса
    field_metro = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')  # Поля заполнения станции метро
    metro = (By.CLASS_NAME, 'select-search__select')  # Выпадающий список
    field_phone = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')  # Поле заполнения телефона

    next_button = (By.XPATH, './/button[text()="Далее"]')  # Кнопка 'далее' на первой странице заказа
    field = (By.ID, 'root')  # Страница(для загрузки ее целиком)