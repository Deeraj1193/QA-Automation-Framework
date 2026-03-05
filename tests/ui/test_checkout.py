from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart()

    inventory_page.open_cart()

    checkout_page.click_checkout()

    checkout_page.enter_checkout_information(
        "John",
        "Doe",
        "12345"
    )

    checkout_page.continue_checkout()

    checkout_page.finish_checkout()

    success_message = checkout_page.get_success_message()

    assert "Thank you for your order!" in success_message
    #assert "Order failed" in success_message