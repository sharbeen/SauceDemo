from pages.cartpage import CartPage


class InventoryPage:
    def __init__(self,page):
        self.page = page

    def selectProducts(self):
        self.page.get_by_text("Sauce Labs Backpack", exact=True).click()
        self.page.locator("#add-to-cart").click()
        self.page.locator("#back-to-products").click()

        self.page.get_by_text("Sauce Labs Bolt T-Shirt", exact=True).click()
        self.page.locator("#add-to-cart").click()
        self.page.locator("#back-to-products").click()

        self.page.get_by_text("Sauce Labs Fleece Jacket", exact=True).click()
        self.page.locator("#add-to-cart").click()
        self.page.locator("#back-to-products").click()
        self.page.locator(".shopping_cart_link").click()
        cart_page = CartPage(self.page)
        return cart_page

