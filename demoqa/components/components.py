from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    def __init__(self, driver, locator, timeout=10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout

    def find_element(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator))
        )

    def click(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator))
        )
        element.click()

    def get_text(self):
        return self.find_element().text
