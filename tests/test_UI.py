import allure
import pytest
from selenium import webdriver
from Pages.page_ui import BasePage


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window() 
    driver.implicitly_wait(100)
    yield driver
    driver.quit()

@allure.id("Тест-1")
@allure.severity ("Blocker")
@allure.title("Поиск актера")
@allure.description("Поиск актера 'Брэд Питт' в шапке страницы в поле поиск")
def test_search_actor(chrome_browser):
    with allure.step("Открытие главной страницы"):
        chrome_browser.get("https://www.kinopoisk.ru")
        page = BasePage(chrome_browser)
    with allure.step("Проверка поиск в шапке страницы актера"):
        assert page.search("Брэд Питт", "suggest-item-person-25584", 'h1[data-tid="f22e0093"]') == "Брэд Питт"

@allure.id("Тест-2")
@allure.severity ("Critical")
@allure.title("Переход в Топ-250 фильмов")
@allure.description("Переход на страницу с результатами поиска Топ-250 фильмов")
def test_top_250(chrome_browser):
    with allure.step("Открытие главной страницы"):
        chrome_browser.get("https://www.kinopoisk.ru")
        page = BasePage(chrome_browser)
    with allure.step("Переход на страницу Топ-250 фильмов"):
        page.top_250()

@allure.id("Тест-3")
@allure.severity ("Critical")
@allure.title("Покупка билетов в кино")
@allure.description("Переход на страницу для покупки билетов в кино")
def test_buy_ticket(chrome_browser):
    with allure.step("Открытие главной страницы"):
        chrome_browser.get("https://www.kinopoisk.ru")
        page = BasePage(chrome_browser)
    with allure.step("Проскролить страницу до нужного элемента"):
        page.scroll()
    with allure.step("Переход на страницу для покупки билетов в кино"):
        page.buy_ticket()

@allure.id("Тест-4")
@allure.severity ("Critical")
@allure.title("Выбор сериала")
@allure.description("Переход на страницу с сериалами")
def test_series(chrome_browser):
    with allure.step("Открытие главной страницы"):
        chrome_browser.get("https://www.kinopoisk.ru")
        page = BasePage(chrome_browser)
    with allure.step("Переход на страницу с сериалами"):
        page.series()

@allure.id("Тест-5")
@allure.severity ("Blocker")
@allure.title("Служба поддержки")
@allure.description("Переход на страницу с сериалами")
def test_support_service(chrome_browser):
    with allure.step("Открытие главной страницы"):
        chrome_browser.get("https://www.kinopoisk.ru")
        page = BasePage(chrome_browser)
    with allure.step("Проскролить страницу до нужного элемента"):
        page.scroll()
    with allure.step("Нажатие на кнопку 'Служба поддержки'"):
        page.support_service()

