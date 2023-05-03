from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Main(Page):
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    TERMS_OF_SERVICE_TITLE = (By.CSS_SELECTOR, 'div.shopify-policy__title')
    SHOP_BY_PRODUCT = (By.XPATH, '//span[text()="Shop by Product" and @class="label"]')
    SHOP_BY_CATEGORY = (By.XPATH, '//span[text()="Shop by Category" and @class="label"]')
    FACE_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Face"]')
    FACE_WASHES_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Face Washes"]')
    FACE_WASH_VERIFICATION = (By.CSS_SELECTOR, 'label[for="Filter-Product type-1"]')
    SUNSCREENS_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Sunscreens"]')
    SUNSCREEN_PRODUCT = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/sun-protection/products/sunscreen-spf-30"]')
    SUNSCREEN_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title h1.h2')
    FACE_PRODUCT = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/gentle-cleanse-face-foam"]')
    FACE_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def click_on_tos(self):
        self.click(*self.TERMS_OF_SERVICE)

    def click_shop_by_prod(self):
        self.click(*self.SHOP_BY_PRODUCT)

    def click_on_face_washes(self):
        sleep(1)
        # self.driver.wait.until(EC.element_to_be_clickable(*self.FACE_WASHES_BUTTON)).click()
        self.click(*self.FACE_WASHES_BUTTON)

    def click_on_sunscreens(self):
        sleep(1)
        self.click(*self.SUNSCREENS_BUTTON)

    def click_sunscreen_product(self):
        self.click(*self.SUNSCREEN_PRODUCT)

    def click_on_face(self):
        sleep(1)
        self.click(*self.FACE_BUTTON)

    def click_on_shop_by_cat(self):
        self.click(*self.SHOP_BY_CATEGORY)

    def click_on_first_face_product(self):
        self.click(*self.FACE_PRODUCT)

    def verify_tos_opens(self, text):
        self.verify_element(text, *self.TERMS_OF_SERVICE_TITLE)

    def verify_face_wash_shown(self, text):
        self.verify_element(text, *self.FACE_WASH_VERIFICATION)

    def verify_first_product_sunscreen(self, text):
        self.verify_element(text, *self.SUNSCREEN_PRODUCT_TITLE)

    def verify_on_face_page(self, text):
        self.verify_url(text)

    def verify_face_product_title(self, text):
        actual_description = self.driver.find_element(*self.FACE_PRODUCT_TITLE).text

        assert text in actual_description, f"Face is not in product description"








