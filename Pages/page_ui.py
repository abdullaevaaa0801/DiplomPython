import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from tests.constants import Kinopoisk_base_url


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def search(self, params, id, result):
        self.driver.find_element(By.NAME, "kp_query").send_keys(params)
        self.driver.find_element(By.ID, id).click()
        return self.driver.find_element(By.CSS_SELECTOR, result).text