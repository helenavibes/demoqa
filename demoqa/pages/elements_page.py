from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/elements'
        super().__init__(driver, base_url)

        self.central_text = WebElement(driver, 'div.col-12.mt-4.col-md-6')

