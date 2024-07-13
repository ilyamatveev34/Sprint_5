from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import STARTING_PAGE, LOGIN_PAGE, PROFILE_PAGE, EMAIL_TEST, PASSWORD_TEST


class TestPersonalAccount:
    def test_go_to_account_by_personal_account_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(PROFILE_PAGE))

        assert driver.current_url == PROFILE_PAGE

    def test_logout_by_logout_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.SEARCH_LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_PAGE))

        assert driver.current_url == LOGIN_PAGE
