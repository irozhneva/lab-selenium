from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, product_id: int):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'http://54.183.112.233/index.php?route=product/product&product_id={self.product_id}'

    def get_product_name(self) -> str:
        product_name: WebElement = self.driver.find_element(By.TAG_NAME, 'h1')
        return product_name.text

    def get_brand_name(self) -> str:
        brand_name: WebElement = self.driver.find_element(By.XPATH, "//li[text()='Brand: ']/a")
        return brand_name.text

    def get_product_code(self) -> str:
        product_code = self.driver.find_element(By.XPATH, "//li[contains(text(),'Product Code:')]")
        return product_code.text

    def get_product_price(self) -> str:
        product_price: WebElement = self.driver.find_element(By.XPATH, '//li//h2')
        return product_price.text

    def get_product_description(self) -> str:
        product_description: WebElement = self.driver.find_element(By.XPATH, '//p//font')
        return product_description.text
