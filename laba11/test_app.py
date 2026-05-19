import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WebAppTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        if os.getenv('CI'): 
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.file_url = 'file://' + os.path.join(base_path, 'index.html')


    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.driver.get(self.file_url)
        self.assertEqual("Тестовая форма для CI/CD", self.driver.title)

    def test_successful_submission(self):
        self.driver.get(self.file_url)
        self.driver.find_element(By.ID, "name-input").send_keys("Тест Тестов")
        self.driver.find_element(By.ID, "email-input").send_keys("test@example.com")
        self.driver.find_element(By.ID, "submit-button").click()

        message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "status-message"))
        )
        self.assertEqual("Вы успешно зарегистрированы!", message.text)
        self.assertIn("success", message.get_attribute("class"))

    def test_empty_submission(self):
        self.driver.get(self.file_url)
        self.driver.find_element(By.ID, "submit-button").click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "status-message"),         
                "Пожалуйста, заполните все поля."  
            )
        )
        message = self.driver.find_element(By.ID, "status-message")
        self.assertEqual("Пожалуйста, заполните все поля.", message.text)
        self.assertIn("error", message.get_attribute("class"))

    def test_form_elements_exist(self):
        self.driver.get(self.file_url)
        self.assertTrue(self.driver.find_element(By.ID, "name-input").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "email-input").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "submit-button").is_displayed())


if __name__ == '__main__':
    unittest.main()