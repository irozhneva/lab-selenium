import unittest
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pageobject.search_page import SearchPage

test_data = ['apple', 'sony', 'nokia', 'stunning']
search_results_data = [['Apple Cinema 30"', '$110.00'], ['Sony VAIO', '$1,202.00'], "There is no product that matches the search criteria.", ('HP LP3065', 'iMac')]


class SearchPageTest(unittest.TestCase):
    driver = None
    search_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.search_page = SearchPage(cls.driver)
        cls.search_page.open()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_search_product_info(self):
        self.search_page.clear_search_field()
        for i in range(1):
            self.search_page.enter_search_words_to_search_field(test_data[i])
            self.search_page.click_search()
            self.assertEqual(
                search_results_data[i],
                self.search_page.get_search_results()
            )

    def test_no_product_found(self):
        self.search_page.clear_search_field()
        self.search_page.enter_search_words_to_search_field(test_data[2])
        self.search_page.click_search()
        self.assertEqual(
            search_results_data[2],
            self.search_page.get_alert_text()
        )

    def test_found_many_products(self):
        self.search_page.clear_search_field()
        self.search_page.enter_search_words_to_search_field(test_data[3])
        self.search_page.click_search_in_product_description_checkbox()
        self.search_page.click_search()
        self.assertEqual(
            search_results_data[3],
            self.search_page.get_search_results_many_products()
        )





