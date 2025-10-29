from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest


@pytest.fixture
def setup_browser():
    options = webdriver.FirefoxOptions()
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_payment_methods(setup_browser):
    driver = setup_browser
    driver.get("https://itcareerhub.de/ru")
    payment_methods_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods_link.click()
    sleep(1)
    driver.save_screenshot("payment_methods.png")


