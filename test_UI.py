import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.page_ui import BasePage


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window() 
    driver.implicitly_wait(100)
    yield driver
    driver.quit()


def test_search_actor(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru")
    page = BasePage(chrome_browser)
    assert page.search("Брэд Питт", "suggest-item-person-25584", 'h1[data-tid="f22e0093"]') == "Брэд Питт"
