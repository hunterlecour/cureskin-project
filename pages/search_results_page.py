from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Search_Result(Page):
    LOGO_HEADER = (By.XPATH, '//a[@class="header__heading-link focus-inset"]')
    PRODUCT_RESULTS = (By.ID, 'ProductCount')
    UNDER_EYE_GEL_PRODUCT_LISTING_TEXT = (By.XPATH, '//a[contains(text(), "Under Eye Gel")]')
    UNDER_EYE_GEL_PRODUCT_LISTING_IMG = (By.XPATH, '//img[@alt="Under Eye Gel"and @loading="lazy"]')
    UNDER_EYE_PRODUCT_PAGE_TITLE = (By.CSS_SELECTOR, 'div.product__title h1.h2')
    SORT_BY_FILTER = (By.CSS_SELECTOR, 'details.facet-filters__sort')
    FILTER_PLUS = (By.CSS_SELECTOR, 'span.facets__open.button.button--small')
    FACE_WASH_CHECKBOX = (By.XPATH, '//label[@class="facet-checkbox"]//span[@class="icon"]')
    FACE_WASH_FILTER_TEXT = (By.CSS_SELECTOR, 'a.active-facets__button[href="/search?options%5Bprefix%5D=last&q=cure&sort_by=relevance"]')
    APPLY_BUTTON = (By.CSS_SELECTOR, 'button.no-js-hidden.button.button--small')
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'a.active-facets__button.active-facets__button--dark')
    PRICE_HIGH_LOW = (By.XPATH, '//label[@for="Filter-price-descending-3"]')
    CURE_PRICES = (By.CSS_SELECTOR, 'span.price-item.price-item--sale')
    CURE_IMAGES = (By.CSS_SELECTOR, 'lazy-image.image-animate.media.media--portrait.media--hover-effect')
    CURE_NAMES = (By.CSS_SELECTOR, 'a.card-information__text.h4')
    UNDER_EYE_GEL = (By.CSS_SELECTOR, '.card__media.media-wrapper[href="/products/under-eye-gel?_pos=1&_sid=cf0af758c&_ss=r"]')

    def open_search_result_cure(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_logo_header(self):
        self.click(*self.LOGO_HEADER)

    def sort_by_filter(self):
        self.wait_for_element_click(*self.SORT_BY_FILTER)

    def high_to_low(self):
        self.wait_for_element_click(*self.PRICE_HIGH_LOW)
        sleep(2)

    def filter_plus(self):
        self.wait_for_element_click(*self.FILTER_PLUS)

    def face_wash_1(self):
        self.wait_for_element_click(*self.FACE_WASH_CHECKBOX)
        self.wait_for_element_click(*self.APPLY_BUTTON)
        sleep(2)

    def clear_all(self):
        self.wait_for_element_click(*self.CLEAR_BUTTON)
        sleep(2)

    def verify_face_wash_filter(self, text):
        self.verify_element(text, *self.FACE_WASH_FILTER_TEXT)

    def verify_high_low(self):
        cure_prices = self.find_elements(*self.CURE_PRICES)
        first_price = cure_prices[0].text.replace('Rs.', '')
        last_price = cure_prices[-1].text.replace('Rs.', '')
        assert first_price > last_price, f"Prices are not filtered from high to low"

    def verify_on_main_page(self, text):
        self.verify_url(text)

    def verify_23_products(self, text):
        self.verify_element(text, *self.PRODUCT_RESULTS)

    def verify_img_name_price(self):
        number_of_products = 8
        for i in range(0, number_of_products):
            assert self.find_elements(*self.CURE_PRICES)[i]
            assert self.find_elements(*self.CURE_NAMES)[i]
            assert self.find_elements(*self.CURE_IMAGES)[i]








