from poms.google import SearchPage, ResultsPage
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def print_results(results):
    print('\nSe encontraron los siguientes resultados:')
    for i in results:
        print(i)
    print('\n_________________________')


def main():
    opts = Options()
    opts.headless = True
    opts.add_argument('--log-level=3')
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome('./drivers/chromedriver.exe', options=opts)

    search_page = SearchPage(driver)
    while True:
        driver.get('https://www.google.com/')
        text_to_find = input('Google> ')

        if text_to_find == 'done':
            print('Bye!')
            break

        search_page.input(text_to_find)
        search_page.click_search()

        results_page = ResultsPage(driver)
        results = results_page.get_results_titles()

        print_results(results)


if __name__ == '__main__':
    main()
