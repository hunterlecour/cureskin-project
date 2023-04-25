from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Product(Page):
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.product-form__submit.button--secondary')
    SHIPPING_CONFIRM = (By.CSS_SELECTOR, 'a.button.button--secondary')
    VERIFY_CART_PAGE = (By.CSS_SELECTOR, 'h1.title')

    def open_product_page(self):
        self.open_url('https://shop.cureskin.com/products/sunscreen-spf-30')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_cart_confirm(self):
        sleep(2)
        actual_text = self.find_element(*self.SHIPPING_CONFIRM).text
        expected_text = "VIEW CART"
        assert actual_text == expected_text

    def view_my_cart(self):
        self.click(*self.SHIPPING_CONFIRM)

    def verify_cart_page(self):
        actual_text = self.find_element(*self.VERIFY_CART_PAGE).text
        expected_result = "Your cart"
        assert actual_text == expected_result
