from playwright.sync_api import Page

from pages.checkout_info_page import CheckoutInfoPage


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def checkout(self):
        self.page.locator("#checkout").click()
        checkout_info_page = CheckoutInfoPage(self.page)
        return checkout_info_page