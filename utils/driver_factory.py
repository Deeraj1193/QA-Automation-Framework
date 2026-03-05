from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def create_driver(headless=False):

        options = Options()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        # FORCE correct ChromeDriver version
        service = Service(ChromeDriverManager(driver_version="145").install())

        driver = webdriver.Chrome(service=service, options=options)

        return driver