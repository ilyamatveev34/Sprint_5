from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import STARTING_PAGE, EMAIL_TEST, PASSWORD_TEST


class TestEntry:
    def test_entry_by_login_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE

    def test_entry_by_personal_account_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE

    def test_entry_by_registration_screen_login_button_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys("ilyamatveev1@gmail.com")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys("elirose")
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE

    def test_entry_by_password_restoration_login_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_PASSWORD_RESTORATION_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PASSWORD_RESTORATION_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE
