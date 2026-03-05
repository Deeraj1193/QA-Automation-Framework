from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart()

    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"

    inventory_page.open_cart()

    assert "cart" in driver.current_url