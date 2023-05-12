from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Main(Page):
    REFUND_POLICY = (By.XPATH, '//a[@href="/policies/refund-policy"]')
    PRIVACY_POLICY = (By.XPATH, '//a[@href="/policies/privacy-policy"]')
    SHIPPING_POLICY = (By.XPATH, '//a[@href="/policies/shipping-policy"]')
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    TERMS_OF_SERVICE_TITLE = (By.CSS_SELECTOR, 'div.shopify-policy__title')
    SEARCH_BAR_ICON = (By.CSS_SELECTOR, 'summary.header__icon svg.modal__toggle-open')
    SEARCH_BAR = (By.CSS_SELECTOR, ".search.search-modal__form #Search-In-Modal")
    SHOP_BY_PRODUCT = (By.XPATH, '//span[text()="Shop by Product" and @class="label"]')
    SHOP_BY_CATEGORY = (By.XPATH, '//span[text()="Shop by Category" and @class="label"]')
    BODY_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Body"]')
    FACE_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Face"]')
    FACE_WASHES_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Face Washes"]')
    FACE_WASH_VERIFICATION = (By.CSS_SELECTOR, 'label[for="Filter-Product type-1"]')
    SUNSCREENS_BUTTON = (By.CSS_SELECTOR, 'list-menu-item[data-title="Sunscreens"]')
    SUNSCREEN_PRODUCT = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/sun-protection/products/sunscreen-spf-30"]')
    SUNSCREEN_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title h1.h2')
    FACE_PRODUCT = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/gentle-cleanse-face-foam"]')
    FACE_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')
    POP_UP_CLOSE = (By.XPATH, "//button[@class='popup-close']")
    OUR_POLICIES = (By.XPATH, "//h2[contains(text(), 'Our policies')]")
    SPF_PRODUCT_TITLES = (By.CSS_SELECTOR, 'a.card-information__text.h4')
    SEARCH_BAR_SUBMISSION = (By.XPATH, '//button[@type="submit" and @class="predictive-search__item--term button button--small button--full-width"]')
    UNDER_EYE_GEL = (By.CSS_SELECTOR, 'a.card-information__text.h4[href="/products/under-eye-gel?_pos=1&_sid=1df8ae37a&_ss=r"]')
    UNDER_EYE_GEL_PRICE = (By.CSS_SELECTOR, 'span.price-item.price-item--sale')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        self.wait_for_element_click(*self.POP_UP_CLOSE)

    def click_on_tos(self):
        self.wait_for_element_click(*self.OUR_POLICIES)
        self.wait_for_element_click(*self.TERMS_OF_SERVICE)

    def click_on_refund_p(self):
        self.wait_for_element_click(*self.REFUND_POLICY)

    def click_on_privacy_p(self):
        self.wait_for_element_click(*self.PRIVACY_POLICY)

    def click_on_shipping_p(self):
        self.wait_for_element_click(*self.SHIPPING_POLICY)

    def click_shop_by_prod(self):
        self.wait_for_element_click(*self.SHOP_BY_PRODUCT)

    def click_on_face_washes(self):
        self.wait_for_element_click(*self.FACE_WASHES_BUTTON)

    def click_on_sunscreens(self):
        self.wait_for_element_click(*self.SUNSCREENS_BUTTON)

    def click_sunscreen_product(self):
        self.click(*self.SUNSCREEN_PRODUCT)

    def click_on_face(self):
        self.wait_for_element_click(*self.FACE_BUTTON)

    def click_on_shop_by_cat(self):
        self.click(*self.SHOP_BY_CATEGORY)

    def click_on_first_face_product(self):
        self.click(*self.FACE_PRODUCT)

    def click_on_body(self):
        self.wait_for_element_click(*self.BODY_BUTTON)

    def search_bar_icon(self):
        self.wait_for_element_click(*self.SEARCH_BAR_ICON)

    def input_text_spf(self, text):
        self.input_text(*self.SEARCH_BAR, text=text)

    def click_submit(self):
        self.click(*self.SEARCH_BAR_SUBMISSION)

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

    def verify_spf_shown(self, text):
        spf_product_texts = self.driver.find_elements(*self.SPF_PRODUCT_TITLES)
        for i in range(0, 3):
            assert text in spf_product_texts[i].text, f"All results do not have 'SPF' "













