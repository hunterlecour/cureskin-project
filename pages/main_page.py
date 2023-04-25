from selenium.webdriver.common.by import By
from pages.base_page import Page


class Main(Page):
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    TERMS_OF_SERVICE_TITLE = (By.CSS_SELECTOR, 'div.shopify-policy__title')
    LOGO_HEADER = (By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def open_search_result(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_tos(self):
        self.click(*self.TERMS_OF_SERVICE)

    def click_logo_header(self):
        self.click(*self.LOGO_HEADER)

    def verify_tos_opens(self):
        expected_text = 'Terms of service'
        actual_text = self.driver.find_element(*self.TERMS_OF_SERVICE_TITLE).text

        assert expected_text == actual_text, f"Expected{expected_text}, but got {actual_text}"

    def verify_on_main_page(self):
        actual_url = self.driver.current_url
        expected_url = 'https://shop.cureskin.com/'
        assert actual_url == expected_url, f'expected{expected_url} but got {actual_url}'
