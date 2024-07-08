from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators_description import TestLocators


class TestPersonalAccount:
    def test_go_to_account_by_personal_account_button_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys("ilyamatveev1@gmail.com")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys("elirose")
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_logout_by_logout_button_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_ACCOUNT_ENTER).send_keys("ilyamatveev1@gmail.com")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER).send_keys("elirose")
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.SEARCH_LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
