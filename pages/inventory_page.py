from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_to_cart(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )

        # JS click (CI safe)
        self.driver.execute_script("arguments[0].click();", button)

    def get_cart_count(self):

        badge = self.wait.until(
            EC.presence_of_element_located(self.cart_badge)
        )

        return badge.text

    def open_cart(self):

        cart = self.wait.until(
            EC.presence_of_element_located(self.cart_icon)
        )

        # JS click
        self.driver.execute_script("arguments[0].click();", cart)