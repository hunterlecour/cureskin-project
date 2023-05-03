from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Main(Page):
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    TERMS_OF_SERVICE_TITLE = (By.CSS_SELECTOR, 'div.shopify-policy__title')
    SHOP_BY_PRODUCT = (By.XPATH, '//span[text()="Shop by Product" and @class="label"]')
    FACE_WASHES_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Face Washes"]')
    FACE_WASH_VERIFICATION = (By.CSS_SELECTOR, 'label[for="Filter-Product type-1"]')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def click_tos(self):
        self.click(*self.TERMS_OF_SERVICE)

    def click_shop_by_prod(self):
        self.click(*self.SHOP_BY_PRODUCT)
        sleep(1)
        # self.driver.wait.until(EC.element_to_be_clickable(*self.FACE_WASHES_BUTTON)).click()
        self.click(*self.FACE_WASHES_BUTTON)

    def verify_tos_opens(self):
        expected_text = 'Terms of service'
        actual_text = self.driver.find_element(*self.TERMS_OF_SERVICE_TITLE).text

        assert expected_text == actual_text, f"Expected{expected_text}, but got {actual_text}"

    def verify_face_wash_shown(self):
        expected_text = 'Face Wash (1)'
        actual_text = self.driver.find_element(*self.FACE_WASH_VERIFICATION).text

        assert expected_text == actual_text, f"Expected{expected_text}, but got {actual_text}"







