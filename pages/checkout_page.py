from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    checkout_button = (By.ID, "checkout")
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    success_message = (By.CLASS_NAME, "complete-header")

    def click_checkout(self):

        checkout = self.wait.until(
            EC.presence_of_element_located(self.checkout_button)
        )

        self.driver.execute_script("arguments[0].click();", checkout)

    def enter_checkout_information(self, first, last, zip_code):

        self.wait.until(
            EC.presence_of_element_located(self.first_name_input)
        ).send_keys(first)

        self.driver.find_element(*self.last_name_input).send_keys(last)
        self.driver.find_element(*self.postal_code_input).send_keys(zip_code)

    def continue_checkout(self):

        cont = self.wait.until(
            EC.presence_of_element_located(self.continue_button)
        )

        self.driver.execute_script("arguments[0].click();", cont)

    def finish_checkout(self):

        finish = self.wait.until(
            EC.presence_of_element_located(self.finish_button)
        )

        self.driver.execute_script("arguments[0].click();", finish)

    def get_success_message(self):

        msg = self.wait.until(
            EC.presence_of_element_located(self.success_message)
        )

        return msg.text