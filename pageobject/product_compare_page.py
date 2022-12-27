from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class ProductComparePage(BasePage):

    def __init__(self, driver: WebDriver, product_id: int):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'http://54.183.112.233/index.php?route=product/product&product_id={self.product_id}'

    def get_product_name(self) -> str:
        product_name: WebElement = self.driver.find_element(By.TAG_NAME, 'h1')
        return product_name.text

    def get_compare_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'btn-group')]//button[contains(@data-original-title,'Compare this Product')]")

    def click_compare_button(self):
        self.get_compare_button().click()

    def get_alert_text_product_added_to_compare(self) -> str:
        """Сообщение, когда продукт добавлен в сравнение"""
        xpath = "//div[contains(@class,'alert alert-success alert-dismissible')]"
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), f'Success: You have added {self.get_product_name()} to your product comparison!'))
        alert_text = self.driver.find_element(By.XPATH, xpath)
        return alert_text.text







    def open_review_tab(self):
        self.get_review_tab().click()

    def get_continue_button_on_review_tab(self) -> WebElement:
        return self.driver.find_element(By.ID, "button-review")

    def click_continue_button_on_review_tab(self):
        self.get_continue_button_on_review_tab().click()

    def get_4_stars_rating(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div//input[contains(@name,'rating') and contains(@value,'4')]")

    def select_4_stars_rating(self):
        self.get_4_stars_rating().click()

    def get_5_stars_rating(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div//input[contains(@name,'rating') and contains(@value,'5')]")

    def select_5_stars_rating(self):
        self.get_5_stars_rating().click()

    def get_you_name_field_on_review_tab(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-name")

    def enter_you_name_on_review_tab(self, name: str):
        name_field = self.get_you_name_field_on_review_tab()
        name_field.send_keys(name)

    def clear_you_name_field(self):
        name_field = self.get_you_name_field_on_review_tab()
        name_field.clear()

    def get_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-review")

    def enter_review(self, review: str):
        review_field = self.get_review_field()
        review_field.send_keys(review)

    def clear_review_field(self):
        review_field = self.get_review_field()
        review_field.clear()

    def get_alert_text_empty_rating(self) -> str:
        """Сообщение, когда не заполнен рейтинг"""
        xpath = "//div[contains(@class,'alert alert-danger alert-dismissible')]"
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), 'Warning: Please select a review rating!'))
        alert_text = self.driver.find_element(By.XPATH, xpath)
        return alert_text.text

    def get_alert_text_rating_less_25_symbols(self) -> str:
        """Сообщение, когда введенный текст рейтинга меньше 25 символов"""
        xpath = "//div[contains(@class,'alert alert-danger alert-dismissible')]"
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), 'Warning: Review Text must be between 25 and 1000 characters!'))
        alert_text = self.driver.find_element(By.XPATH, xpath)
        return alert_text.text

    def get_alert_product_review_submitted_successful(self) -> str:
        """Сообщение, ревью отправилено успешно"""
        xpath = "//div[contains(@class,'alert alert-success alert-dismissible')]"
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), 'Thank you for your review. It has been submitted to the webmaster for approval.'))
        alert_text = self.driver.find_element(By.XPATH, xpath)
        return alert_text.text





