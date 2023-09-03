import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '1920'
    browser.config.window_width = '1080'
    browser.config.base_url = 'https://dev0skks.etalongroup.com'

    yield

    browser.quit()