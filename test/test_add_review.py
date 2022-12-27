import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pageobject.product_review_page import ProductReviewPage


class AddReviewTest(unittest.TestCase):
    driver = None
    product_review_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.product_review_page = ProductReviewPage(cls.driver, product_id=42)
        cls.product_review_page.open()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_send_empty_review(self):
        self.driver.refresh()
        self.product_review_page.open_review_tab()
        self.product_review_page.clear_you_name_field()
        self.product_review_page.clear_review_field()
        self.product_review_page.click_continue_button_on_review_tab()
        self.assertEqual(
            'Warning: Please select a review rating!',
            self.product_review_page.get_alert_text_empty_rating()
        )

    def test_review_less_than_25_symbols(self):
        self.product_review_page.open_review_tab()
        self.product_review_page.clear_you_name_field()
        self.product_review_page.clear_review_field()
        self.product_review_page.select_4_stars_rating()
        self.product_review_page.enter_you_name_on_review_tab(name="John")
        self.product_review_page.enter_review(review="This is the best product")
        self.product_review_page.click_continue_button_on_review_tab()
        self.assertEqual(
            'Warning: Review Text must be between 25 and 1000 characters!',
            self.product_review_page.get_alert_text_rating_less_25_symbols()
        )

    def test_send_review_success(self):
        self.product_review_page.open_review_tab()
        self.product_review_page.clear_you_name_field()
        self.product_review_page.clear_review_field()
        self.product_review_page.select_5_stars_rating()
        self.product_review_page.enter_you_name_on_review_tab(name="John")
        self.product_review_page.enter_review(review="This is the best product ever")
        self.product_review_page.click_continue_button_on_review_tab()
        self.assertEqual(
            'Thank you for your review. It has been submitted to the webmaster for approval.',
            self.product_review_page.get_alert_product_review_submitted_successful()
        )
