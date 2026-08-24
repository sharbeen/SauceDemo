from playwright.sync_api import Playwright
import pytest

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture
def browser(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context=browser.new_context()
    context.clear_cookies()
    page = context.new_page()
    yield page
    page.close()




