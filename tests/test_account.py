from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestAccountLocators


class TestChromeAccount:

    def test_account_correct_personal_account(self, chromedriver_logged_in):
        chromedriver_logged_in.find_element(*TestAccountLocators.LOCATOR_MAIN_PAGE_PERSONAL_BUTTON).click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        current_url = chromedriver_logged_in.current_url

        # chromedriver_logged_in.quit()

        assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile', 'Не удалось войти в аккаунт через кнопку "личный кабинет" '

    def test_account_correct_konstruct_redirect(self, chromedriver_logged_in):
        chromedriver_logged_in.get("https://stellarburgers.nomoreparties.site/account")

        konstruct, logo = chromedriver_logged_in.find_elements(*TestAccountLocators.LOCATOR_KONSTRUCT_REDIRECT)
        konstruct.click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        after_konstruct_url = chromedriver_logged_in.current_url
        logo.click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        after_logo_url = chromedriver_logged_in.current_url
        # chromedriver_logged_in.quit()
        assert after_konstruct_url == 'https://stellarburgers.nomoreparties.site/', 'Кнопка Конструктор не сработала'

        assert after_logo_url == 'https://stellarburgers.nomoreparties.site/', 'Кнопка лого не сработала'

    def test_account_correct_log_out(self, chromedriver_logged_in):
        chromedriver_logged_in.get('https://stellarburgers.nomoreparties.site/account')
        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        chromedriver_logged_in.find_element(*TestAccountLocators.LOCATOR_LOGOUT).click()
        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = chromedriver_logged_in.current_url

        # chromedriver_logged_in.quit()

        assert current_url == 'https://stellarburgers.nomoreparties.site/login', 'Выход не удался, ну дела'
