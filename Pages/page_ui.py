import allure
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск в шапке страницы в поле поиск")
    def search(self, params, id, result):
        self.driver.find_element(By.NAME, "kp_query").send_keys(params)
        self.driver.find_element(By.ID, id).click()
        return self.driver.find_element(By.CSS_SELECTOR, result).text

    @allure.step("Поиск Топ-250 фильмов")
    def top_250(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Расширенный поиск"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/level/20/"').click()

    @allure.step("Покупка билетов в кино")
    def buy_ticket(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="styles_link__KtvyW"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="styles_root__omMgy styles_item__pq3A4"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/afisha/new/film/5452393/"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'span[class="calendar-filter__title-day"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="day-20"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'span[data-template="schedule-item__template"]').click()

    @allure.step("Проскролить страницу до нужного элемента")
    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,800)")

    @allure.step("Поиск сериалов")
    def series(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/lists/categories/movies/8/"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'img[src="//avatars.mds.yandex.net/get-bunker/50064/546ba464afc21764e58be3987df5063a0a2f9da9/192x192"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/series/502838/"]').click()

    @allure.step("Поиск селектора поддержки")
    def support_service(self):
        self.driver.find_element(By.XPATH, "//button[@class='styles_contentButton__Yfvdh']").click()

        """ Использовать при первом запуске теста """
        # # self.driver.find_element(By.CSS_SELECTOR, 'button[data-test-tag="confirm-dialog-ok"]').click()