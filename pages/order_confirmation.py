from playwright.sync_api import expect


class OrderConfirmation:
    def __init__(self,page):
        self.page = page

    def check_order_confirmation(self):
       print(self.page.locator(".complete-header").text_content())
       expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")


