from selenium.webdriver.common.by import By
from pages.base_page import Page


class Search_Result(Page):
    LOGO_HEADER = (By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')

    def open_search_result_cure(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_logo_header(self):
        self.click(*self.LOGO_HEADER)

    def verify_on_main_page(self):
        actual_url = self.driver.current_url
        expected_url = 'https://shop.cureskin.com/'
        assert actual_url == expected_url, f'expected{expected_url} but got {actual_url}'