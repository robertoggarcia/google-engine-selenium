import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from poms.google import SearchPage
from selenium.common.exceptions import NoSuchElementException


class TestSearchPom(unittest.TestCase):

    def setUp(self) -> None:
        opts = Options()
        opts.headless = False
        self.driver = Chrome('./drivers/chromedriver.exe', options=opts)
        self.driver.get('https://www.google.com/')
        self.search_page = SearchPage(self.driver)

    def test_search_pom_instance(self):
        self.assertNotEqual(self.search_page, None)

    def test_validate_driver(self):
        self.assertNotEqual(self.search_page.driver, None)

    def test_input_method(self):
        self.search_page.input('google')

        input_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[' \
                      '1]/div/div[2]/div/span'
        input_element = self.driver.find_element_by_xpath(input_xpath)

        self.assertEqual(input_element.text, 'google')

    def test_click_search(self):
        self.search_page.input('google')
        self.search_page.click_search()

        self.assertRaises(NoSuchElementException,
                          self.driver.find_element_by_xpath,
                          self.search_page.button_xpath)

    def tearDown(self) -> None:
        self.driver.close()
