from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()

def test_input_text(driver):# Ожидание до 5 секунд
    pole = driver.find_element(By.ID, "newButtonName")
    pole.send_keys("ITCH")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    wait = WebDriverWait(driver, 5)
    result = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "ITCH"))
    assert result