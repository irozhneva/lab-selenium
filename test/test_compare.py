import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pageobject.product_compare_page import ProductComparePage


class CompareTest(unittest.TestCase):
    driver = None
    product_compare_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.product_compare_page = ProductComparePage(cls.driver, product_id=42)
        cls.product_compare_page.open()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_compare_single_product(self):
        self.product_compare_page.get_product_name()
        self.product_compare_page.click_compare_button()
        self.assertEqual(
            f'Success: You have added {self.product_compare_page.get_product_name()} to your product comparison!\n×',
            self.product_compare_page.get_alert_text_product_added_to_compare()
        )
