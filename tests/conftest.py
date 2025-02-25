import pytest
from selenium import webdriver
from urls import home_page

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.get(home_page)
    yield driver
    driver.quit()

