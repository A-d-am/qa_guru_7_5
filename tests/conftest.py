import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    driver_options = browser.config.driver_options = webdriver.FirefoxOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield

    browser.quit()
