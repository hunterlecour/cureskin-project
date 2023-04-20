from pages.main_page import Main


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main(self.driver)
