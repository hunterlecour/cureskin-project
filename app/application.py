from pages.main_page import Main
from pages.search_results_page import Search_Result


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main(self.driver)
        self.search_results_page = Search_Result(self.driver)
