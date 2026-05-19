from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_NAME = (By.CLASS_NAME, "productinfo")

    def search_product(self, product_name):
        self.driver.get("https://automationexercise.com/products")
        self.find(self.SEARCH_INPUT).send_keys(product_name)
        self.find(self.SEARCH_BUTTON).click()