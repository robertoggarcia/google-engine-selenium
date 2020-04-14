import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from poms.google import SearchPage, ResultsPage


class TestResultsPage(unittest.TestCase):

    def setUp(self) -> None:
        opts = Options()
        opts.headless = False
        self.driver = Chrome('./drivers/chromedriver.exe', options=opts)
        self.driver.get('https://www.google.com/')
        search_page = SearchPage(self.driver)
        self.search_term = 'Rock'
        search_page.input(self.search_term)
        search_page.click_search()
        self.result_page = ResultsPage(self.driver)

    def test_results_page_instance(self):
        self.assertNotEqual(self.result_page, None)

    def test_driver(self):
        self.assertNotEqual(self.result_page.driver, None)

    def test_get_results_titles(self):
        results = self.result_page.get_results_titles()

        self.assertIsInstance(results, list)

    def test_get_results_titles_values(self):
        results = self.result_page.get_results_titles()

        self.assertNotEqual(len(results), 0)

    def test_get_results_titles_validate(self):
        results = self.result_page.get_results_titles()
        fail_validation = False
        for item in results:
            words = [word.lower().replace(':', '') for word in item.split()]
            if self.search_term.lower() not in words:
                fail_validation = True
                break

        self.assertNotEqual(fail_validation, True)

    def tearDown(self) -> None:
        self.driver.close()
