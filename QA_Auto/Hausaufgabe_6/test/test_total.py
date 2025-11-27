import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from QA_Auto.Hausaufgabe_6.pages.checkout_page import CheckoutPage
from QA_Auto.Hausaufgabe_6.pages.inventory_page import InventoryPage
from QA_Auto.Hausaufgabe_6.pages.login_page import LoginPage
from QA_Auto.Hausaufgabe_6.pages.cart_page import CartPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_total(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.success_login("standard_user", "secret_sauce")

    inventory.click_add_backpack()
    inventory.click_add_bolt()
    inventory.click_add_onesie()

    inventory.click_open_cart()

    cart.click_checkout()

    login.add_firstname("Ivan")
    login.add_lastname("Ivanov")
    login.add_postalcode("12345678")


    driver.find_element(By.ID, "continue").click()

    checkout = CheckoutPage(driver)
    assert "$58.29" in checkout.get_total()