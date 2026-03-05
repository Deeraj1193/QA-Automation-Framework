import pytest
import os

from utils.driver_factory import DriverFactory
from utils.config import Config


@pytest.fixture(scope="function")
def driver():

    driver = DriverFactory.create_driver(headless=Config.HEADLESS)

    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = f"reports/screenshots/{item.name}.png"

            driver.save_screenshot(screenshot_path)