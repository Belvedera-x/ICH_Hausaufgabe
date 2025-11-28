import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from QA_Auto.Hausaufgabe_6.pages.checkout_page import CheckoutPage
from QA_Auto.Hausaufgabe_6.pages.inventory_page import InventoryPage
from QA_Auto.Hausaufgabe_6.pages.login_page import LoginPage
from QA_Auto.Hausaufgabe_6.pages.cart_page import CartPage
from QA_Auto.Hausaufgabe_6.pages.name_adres_page import NameAdresPage


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")   # добавил режим инкогнито

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


def test_total(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    get_name = NameAdresPage(driver)

    login.success_login("standard_user", "secret_sauce")

    inventory.click_add_backpack()
    inventory.click_add_bolt()
    inventory.click_add_onesie()

    inventory.click_open_cart()

    cart.click_checkout()

    get_name.add_firstname("Ivan")
    get_name.add_lastname("Ivanov")
    get_name.add_postalcode("12345678")
    get_name.get_continue().click()

    checkout = CheckoutPage(driver)
    assert "$58.29" in checkout.get_total()