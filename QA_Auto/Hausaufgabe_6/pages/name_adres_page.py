from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NameAdresPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_firstname_input(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))

    def get_lastname_input(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))

    def get_postalcode_input(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#postal-code")))

    def get_continue(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#continue")))

    def add_firstname(self, firstname):
        firstname_field = self.get_firstname_input()
        # firstname_field.clear()
        firstname_field.send_keys(firstname)

    def add_lastname(self, lastname):
        lastname_field = self.get_lastname_input()
        lastname_field.clear()
        lastname_field.send_keys(lastname)

    def add_postalcode(self, postalcode):
        postalcode_field = self.get_postalcode_input()
        postalcode_field.clear()
        postalcode_field.send_keys(postalcode)
