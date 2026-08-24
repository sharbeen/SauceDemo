from playwright.sync_api import expect

from pages.order_confirmation import OrderConfirmation


class CheckoutFinalPage:
    def __init__(self, page):
        self.page = page

    def checkout_final_conf(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Overview")
        self.page.get_by_text("Finish").click()
        order_confirmation_page =OrderConfirmation(self.page)
        return order_confirmation_page
