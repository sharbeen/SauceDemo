from playwright.sync_api import Page

from pages.checkout_finalpage import CheckoutFinalPage


class CheckoutInfoPage:
    def __init__(self, page: Page):
        self.page = page

    def add_checkout_info(self,firstName,lastName,postcode):
        self.page.locator("#first-name").fill(firstName)
        self.page.locator("#last-name").fill(lastName)
        self.page.locator("#postal-code").fill(postcode)
        self.page.locator("#continue").click()
        checkout_final_page = CheckoutFinalPage(self.page)
        return checkout_final_page



