import pytest

from pages.login_page import LoginPage
from utils.logger import get_logger

def test_valid_login(driver):

    logger = get_logger("test_valid_login")
    logger.info("Starting valid login test")

    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")

    logger.info("Login action executed")

    assert "inventory" in driver.current_url

    logger.info("Valid login test passed")


def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message()

    assert "Epic sadface" in error_message