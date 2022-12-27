from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def get_search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.ID, "input-search")
        return search_field

    def get_search_button(self) -> WebElement:
        return self.driver.find_element(By.ID, "button-search")

    def get_alert_text(self) -> str:
        """Сообщение, когда нет результатов поисков"""
        alert_text = self.driver.find_element(By.XPATH, '//div/p[2]')
        return alert_text.text

    def enter_search_words_to_search_field(self, search_words: str):
        """Ввести поисковые слова"""
        search_field = self.get_search_field()
        search_field.send_keys(search_words)

    def clear_search_field(self):
        """Очистить поле поиска"""
        search_field = self.get_search_field()
        search_field.clear()

    def click_search(self):
        """Поиск"""
        self.get_search_button().click()

    def get_search_results(self) -> list[str]:
        """"Поиск названия продукта и цены"""
        search_results_product_name: WebElement = self.driver.find_element(By.XPATH, '//h4')
        search_results_price: WebElement = self.driver.find_element(By.CLASS_NAME, 'price-new')
        search_results: list[str] = []
        product_name = search_results_product_name.text
        price = search_results_price.text
        search_results.append(product_name)
        search_results.append(price)
        return search_results

    def click_search_in_product_description_checkbox(self):
        """Выбрать  “Search in product descriptions” чекбокс"""
        search_in_product_description_checkbox: WebElement = self.driver.find_element(By.ID, 'description')
        search_in_product_description_checkbox.click()

    def get_search_results_many_products(self):
        """Поиск нескольких продуктов"""
        xpath1: WebElement = self.driver.find_element(By.XPATH, "//div[1][contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]//h4//a")
        xpath2: WebElement = self.driver.find_element(By.XPATH, "//div[2][contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]//h4//a")
        product1 = xpath1.text
        product2 = xpath2.text
        return product1, product2






