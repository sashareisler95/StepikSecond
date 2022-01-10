import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="Choose lang"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
