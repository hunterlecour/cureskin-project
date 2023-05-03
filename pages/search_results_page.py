from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Search_Result(Page):
    LOGO_HEADER = (By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')
    PRODUCT_RESULTS = (By.ID, 'ProductCount')

    def open_search_result_cure(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_logo_header(self):
        self.click(*self.LOGO_HEADER)

    def verify_on_main_page(self):
        actual_url = self.driver.current_url
        expected_url = 'https://shop.cureskin.com/'
        assert actual_url == expected_url, f'expected{expected_url} but got {actual_url}'

    def verify_23_products(self):
        actual_text = self.driver.find_element(*self.PRODUCT_RESULTS).text
        expected_text = '23 results found for “cure”'
        assert actual_text == expected_text, f'Should of gotten {expected_text}, but received {actual_text}'