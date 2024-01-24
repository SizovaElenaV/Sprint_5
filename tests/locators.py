from selenium.webdriver.common.by import By


class TestLoginLocators:
    LOCATOR_LOGIN_PAGE_MAIL_PASS_FIELD = (By.XPATH,
                                          "//input[@class='text input__textfield "
                                          "text_type_main-default']")
    LOCATOR_LOGIN_PAGE_LOGIN_BUTTON = (By.XPATH,
                                       "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx"
                                       " button_button_size_medium__3zxIa']")
    LOCATOR_MAIN_PAGE_LOGIN_BUTTON = (By.XPATH,
                                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                      "button_button_size_large__G21Vg']")

    LOCATOR_MAIN_PAGE_PERSONAL_LOGIN_BUTTON = (By.XPATH,
                                               "//a[@href='/account']")
    LOCATOR_REGISTER_PAGE_LOGIN_BUTTON = (By.XPATH,
                                          "//a[@href='/login']")
    LOCATOR_FORGOTPAS_PAGE_LOGIN_BUTTON = (By.XPATH,
                                           "//a[@href='/login']")


class TestAccountLocators:
    LOCATOR_MAIN_PAGE_PERSONAL_BUTTON = (By.XPATH,
                                         "//a[@href='/account']")
    LOCATOR_KONSTRUCT_REDIRECT = (By.XPATH,
                                  "//a[@href='/']")
    LOCATOR_LOGOUT = (By.XPATH,
                      "//button[@class='Account_button__14Yp3 text text_type_main-medium "
                      "text_color_inactive']")


class TestKonstruktLocators:
    LOCATOR_SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    LOCATOR_NACHINKA = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']")
    LOCATOR_BULKA = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")


class TestRegistrationLocators:
    LOCATOR_REGISTRATION_PAGE_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 "
                                                  "button_button_type_primary__1O7Bx "
                                                  "button_button_size_medium__3zxIa']")
