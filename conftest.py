import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def default_lang(parser):
    parser.addoption('--accept_languages', action='store', default="ru",
                     help="Choose language: ")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("lang")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
