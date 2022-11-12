from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


URL_TEMPLATE = (
    'https://www.avito.ru'  # /irkutsk?q=самовар'
)


def count_adverts(url: str, region: str, phrase: str) -> int:
    """
    Parse page.
    """
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except WebDriverException:
        '''ser = Service(
            ChromeDriverManager().install()
        )
        '''
        # driver = webdriver.Chrome(service=ser, options=chrome_options)

    try:
        driver.get('{}/{}?q={}'.format(url, region, phrase))
    except InvalidArgumentException:
        driver.close()
        return ''

    html = driver.page_source
    soup = bs(html, 'html.parser')
    adverts_counter = soup.find_all(
        'span',
        attrs={'data-marker': 'page-title/count'}
    )
    if adverts_counter:
        return adverts_counter[0].text
    return 0


def main():
    print(count_adverts(URL_TEMPLATE, 'tula', 'самовар'))


if __name__ == '__main__':
    main()
