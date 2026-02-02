import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    page.set_default_timeout(15000)

    yield page
    page.close()
