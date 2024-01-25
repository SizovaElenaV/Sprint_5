from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestKonstruktLocators


class TestChromeKonstrukt:
    """
    При корректном скролле элементов класс объектов (булка, начинка или совус) принимает значение,
    равное 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect', на этом и построен этот тест
    """
    def test_konstrukt_correct_sauce_scroll(self, chromedriver_bulka_sauce_nachinka):
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        sauce.click()
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(TestKonstruktLocators.LOCATOR_SAUCE))
        sauce_class = sauce.get_attribute('class')

        # chrome_driver.quit()

        assert sauce_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_konstrukt_correct_nachinka_scroll(self, chromedriver_bulka_sauce_nachinka):
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        nachinka.click()

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(TestKonstruktLocators.LOCATOR_NACHINKA))
        nachinka_class = nachinka.get_attribute('class')

        # chrome_driver.quit()

        assert nachinka_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_konstrukt_correct_bulka_scroll(self, chromedriver_bulka_sauce_nachinka):
        """
        Чтобы проверить как работает скролл для булочки, нужно сначала проскроллить до других объектов,
        потом уже прожимать кнопку булочка и проверять, успешен ли скролл
        """
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        nachinka.click()
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(TestKonstruktLocators.LOCATOR_NACHINKA))
        bulka.click()
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(TestKonstruktLocators.LOCATOR_BULKA))
        bulka_class = bulka.get_attribute('class')

        # chrome_driver.quit()

        assert bulka_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
