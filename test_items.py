from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


def test_button(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException:
        print('I do not found button!')
