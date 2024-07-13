from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import STARTING_PAGE, EMAIL_TEST, PASSWORD_TEST


class TestConstructor:
    def test_go_to_constructor_by_constructor_button_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_CONSTUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE

    def test_go_to_constructor_by_logo_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys(EMAIL_TEST)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_WEBSITE_LOGO).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(STARTING_PAGE))

        assert driver.current_url == STARTING_PAGE

    def test_switch_to_sauces_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_TAB_SAUCES).click()

        assert driver.find_element(*TestLocators.SEARCH_TAB_SAUCES_ACTIVE).is_displayed()

    def test_switch_to_fillings_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()

        assert driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS_ACTIVE).is_displayed()

    def test_switch_to_buns_success(self, driver):
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()
        driver.find_element(*TestLocators.SEARCH_TAB_BUNS).click()

        assert driver.find_element(*TestLocators.SEARCH_TAB_BUNS_ACTIVE).is_displayed()
