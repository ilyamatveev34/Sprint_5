import pytest
from selenium import webdriver

from helpers import login_generator


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def email_generator():
    domain = 'gmail.com'
    email, name = login_generator(domain)
    return email, name
