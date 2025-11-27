from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

   def get_backpack_to_cart(self):
       return self.wait.until(EC.presence_of_element_located((
           By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack')))


   def get_bolt_to_cart(self):
       return self.wait.until(EC.presence_of_element_located((
           By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt')))


   def get_onesie_to_cart(self):
       return self.wait.until(EC.presence_of_element_located((
           By.CSS_SELECTOR,'#add-to-cart-sauce-labs-onesie')))


   def open_cart(self):
       return self.wait.until(EC.presence_of_element_located((
           By.CSS_SELECTOR,'#shopping_cart_container')))


   def click_add_backpack(self):
       self.get_backpack_to_cart().click()


   def click_add_bolt(self):
       self.get_bolt_to_cart().click()

   def click_add_onesie(self):
       self.get_onesie_to_cart().click()

   def click_open_cart(self):
       self.open_cart().click()



