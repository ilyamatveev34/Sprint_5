from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators_description import TestLocators


class TestRegistration:
    def test_registration_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME_REGISTRATION).send_keys("Ilia")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_REGISTRATION).send_keys("ilyamatveev1@gmail.com")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_REGISTRATION).send_keys("elirose")
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_password_too_short_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME_REGISTRATION).send_keys("Ilia")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_REGISTRATION).send_keys("ilyamatveev1@gmail.com")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_REGISTRATION).send_keys("elir")
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INCORRECT_PASSWORD_MESSAGE))

        assert driver.find_element(*TestLocators.SEARCH_INCORRECT_PASSWORD_MESSAGE).text == 'Некорректный пароль'
