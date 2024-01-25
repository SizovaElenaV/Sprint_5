from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestLoginLocators


class TestChromeLogin:

    def _login_page_filler(self, chrome_driver):
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        self.after_button_click_url = chrome_driver.current_url

        mail_field, pass_field = chrome_driver.find_elements(*TestLoginLocators.LOCATOR_LOGIN_PAGE_MAIL_PASS_FIELD)

        mail_field.send_keys('231@mail.ru')
        pass_field.send_keys('postgres')

        chrome_driver.find_element(*TestLoginLocators.LOCATOR_LOGIN_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        return chrome_driver.current_url

    def test_login_correct_login_to_account(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site")
        chrome_driver.find_element(*TestLoginLocators.LOCATOR_MAIN_PAGE_LOGIN_BUTTON).click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        # chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'было перехода по кнопке "Войти в аккаунт'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_correct_login_personal_account(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site")
        chrome_driver.find_element(*TestLoginLocators.LOCATOR_MAIN_PAGE_PERSONAL_LOGIN_BUTTON).click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        # chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Личный Кабинет" '
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_correct_login_in_register(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/register")
        chrome_driver.find_element(*TestLoginLocators.LOCATOR_REGISTER_PAGE_LOGIN_BUTTON).click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        # chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме регистрации'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_correct_login_in_forgot_password(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        chrome_driver.find_element(*TestLoginLocators.LOCATOR_FORGOTPAS_PAGE_LOGIN_BUTTON).click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        # chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме восстановления пароля'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'
