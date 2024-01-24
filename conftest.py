import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def _chrome_driver():
    return webdriver.Chrome()


@pytest.fixture
def chrome_driver():
    chrome_driver = _chrome_driver()
    yield chrome_driver
    chrome_driver.quit()




@pytest.fixture
def chromedriver_name_mail_pass_fields(chrome_driver):
    chrome_d = chrome_driver
    chrome_d.get("https://stellarburgers.nomoreparties.site/register")
    name_field, mail_field, pass_field = chrome_d.find_elements(By.XPATH,
                                                                "//input[@class='text input__textfield "
                                                                "text_type_main-default']")
    return chrome_d, name_field, mail_field, pass_field



@pytest.fixture
def chromedriver_logged_in(chrome_driver):
    chrome_d = chrome_driver
    chrome_d.get("https://stellarburgers.nomoreparties.site/login")

    mail_field, pass_field = chrome_d.find_elements(By.XPATH,
                                                    "//input[@class='text input__textfield "
                                                    "text_type_main-default']")

    mail_field.send_keys('231@mail.ru')
    pass_field.send_keys('postgres')

    chrome_d.find_element(By.XPATH,
                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx"
                          " button_button_size_medium__3zxIa']").click()

    WebDriverWait(chrome_d, 5).until(
        expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    return chrome_d


@pytest.fixture
def chromedriver_bulka_sauce_nachinka(chrome_driver):
    chrome_d = chrome_driver
    chrome_d.get('https://stellarburgers.nomoreparties.site/')
    bulka, sauce, nachinka = chrome_d.find_elements(By.XPATH,
                                                    "//div[contains(@style,'display: flex')]//div")

    return chrome_d, bulka, sauce, nachinka
