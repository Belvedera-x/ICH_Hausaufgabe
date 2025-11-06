from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_logo(driver):
    driver.get("https://itcareerhub.de/ru")
    logo_ich = driver.find_element(By.CSS_SELECTOR, ".tn-elem__13452582811710153310155")
    assert logo_ich.is_displayed()

def test_link_program(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.LINK_TEXT, "Программы")
    assert link.is_displayed()

def test_link_pay(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert link.is_displayed()

def test_link_nachricht(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.LINK_TEXT, "Новости")
    assert link.is_displayed()

def test_link_wir(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.LINK_TEXT, "О нас")
    assert link.is_displayed()

def test_link_bewertungen(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link.is_displayed()

def test_batton_de(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.CSS_SELECTOR, ".tn-elem__13452582811710152941400")
    assert link.is_displayed()

def test_batton_ru(driver):
    driver.get("https://itcareerhub.de/ru")
    link = driver.find_element(By.CSS_SELECTOR, ".tn-elem__13452582811710152827519")
    assert link.is_displayed()

def test_phone(driver):
    driver.get("https://itcareerhub.de/ru/contact-us#popup-close")
    phone = driver.find_element(By.CSS_SELECTOR, ".tn-elem__11949824661710153310161")
    phone.click()
    driver.implicitly_wait(5)
    click_text = driver.find_element(By.TAG_NAME, "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами")
    assert click_text.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"


