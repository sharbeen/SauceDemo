import json
from playwright.sync_api import Page, expect

from pages import checkout_info_page
from pages.loginpage import LoginPage

with open('data/testdata.json') as f:
    testdata = json.load(f)  # load is a method to convert json to python object
    user_credentials_list = testdata["user_credentials"]
    user_info_list = testdata["user_info"]

def test_saucedemo(page:Page):
    username=user_credentials_list[0]["username"]
    password = user_credentials_list[0]["password"]
    firstName=user_info_list[0]["FirstName"]
    lastName=user_info_list[0]["LastName"]
    postcode=user_info_list[0]["PostCode"]

    login_page = LoginPage(page)
    login_page.navigate_to()
    inventory_page = login_page.login(username,password)
    cart_page = inventory_page.selectProducts()
    checkout_info_page = cart_page.checkout()
    checkout_final_page = checkout_info_page.add_checkout_info(firstName,lastName,postcode)
    order_confirmation_page = checkout_final_page.checkout_final_conf()
    order_confirmation_page.check_order_confirmation()















