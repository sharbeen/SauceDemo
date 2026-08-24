from playwright.sync_api import Page
from pages.inventorypage import InventoryPage
import json

from conftest import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

    def navigate_to(self, path: str = ""):
        """Navigate to a URL"""
        url = self.base_url + path if path else self.base_url
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()
        inventory_page = InventoryPage(self.page)
        return inventory_page