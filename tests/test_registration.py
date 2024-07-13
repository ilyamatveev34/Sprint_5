from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import STARTING_PAGE, LOGIN_PAGE, PASSWORD_TEST


class TestRegistration:
    def test_registration_success(self, driver, email_generator):
        email, name = email_generator
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME_REGISTRATION).send_keys(name)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_REGISTRATION).send_keys(PASSWORD_TEST)
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_PAGE))

        assert driver.current_url == LOGIN_PAGE

    def test_password_too_short_failed(self, driver, email_generator):
        email, name = email_generator
        driver.get(STARTING_PAGE)

        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME_REGISTRATION).send_keys(name)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_REGISTRATION).send_keys("elir")
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INCORRECT_PASSWORD_MESSAGE))

        assert driver.find_element(*TestLocators.SEARCH_INCORRECT_PASSWORD_MESSAGE).text == 'Некорректный пароль'
