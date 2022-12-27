import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pageobject.product_page import ProductPage

test_data = {
    "product_name": 'Apple Cinema 30"',
    "product_brand": "Apple",
    "product_code": "Product Code: Product 15",
    "product_price": "$110.00",
    "sentence_in_product_description": "The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution"
}


class ProductPageTest(unittest.TestCase):
    driver = None
    product_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.product_page = ProductPage(cls.driver, product_id=42)
        cls.product_page.open()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_product_name_is_present(self):
        self.assertEqual(
            test_data["product_name"],
            self.product_page.get_product_name()
        )

    def test_product_brand_is_present(self):
        self.assertEqual(
            test_data["product_brand"],
            self.product_page.get_brand_name()
        )

    def test_product_code_is_present(self):
        self.assertEqual(
            test_data["product_code"],
            self.product_page.get_product_code()
        )

    def test_product_price_is_present(self):
        self.assertEqual(
            test_data["product_price"],
            self.product_page.get_product_price()
        )

    def test_part_of_product_description_is_present(self):
        self.assertIn(
            test_data["sentence_in_product_description"],
            self.product_page.get_product_description()
        )
