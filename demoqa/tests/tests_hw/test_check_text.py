from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    page = DemoQA(browser)
    page.visit()
    assert page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_center_text_on_elements_page(browser):
    demo_page = DemoQA(browser)
    elements_page = ElementsPage(browser)
    demo_page.visit()
    demo_page.btn_elements.click()
    assert elements_page.central_text.get_text() == 'Please select an item from left to start practice.'