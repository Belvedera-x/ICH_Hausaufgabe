import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_iframe_text(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe"))
    )
    expected_text = "semper posuere integer et senectus justo curabitur."
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    found = any(expected_text in p.text for p in paragraphs)
    driver.switch_to.default_content()
    assert found, "Текст не найден внутри iframe"

def test_dragging(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 5)
    click_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.fc-button.fc-cta-consent")
    ))
    click_btn.click()
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))))
    source = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery  li:nth-child(1)")))
    target = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash")))
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()