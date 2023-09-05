import pytest
from selene import browser
import os

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '1920'
    browser.config.window_width = '1080'
    browser.config.base_url = 'https://dev0skks.etalongroup.com'

    login1 = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    yield

    browser.quit()