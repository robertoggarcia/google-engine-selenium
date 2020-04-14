import time


class SearchPage:
    driver = None
    input_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
    button_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'

    def __init__(self, driver):
        self.driver = driver

    def input(self, text):
        input_element = self.driver.find_element_by_xpath(self.input_xpath)
        input_element.clear()
        input_element.send_keys(text)

    def click_search(self):
        button = self.driver.find_element_by_xpath(self.button_xpath)
        self.driver.execute_script("arguments[0].click();", button)


class ResultsPage:
    driver = None
    results_titles_xpath = '//h3[@class="LC20lb DKV0Md"]'

    def __init__(self, driver):
        self.driver = driver

    def get_results_titles(self):
        results = self.driver.find_elements_by_xpath(self.results_titles_xpath)
        return [item.text for item in results if item.text]
