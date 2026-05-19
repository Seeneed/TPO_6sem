import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def make_screenshot(self, name):
        if not os.path.exists("screenshots"): os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")

    def get_cookies(self):
        return self.driver.get_cookies()