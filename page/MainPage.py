from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.chitai-gorod.ru"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def book_search(self, book_title: str) -> None:
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').send_keys(book_title)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Найти"]').click()

    def result_search(self) -> str:
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h1.search-title__head'))))

        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.search-title__head').text

    def message_result_search(self) -> str:
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h4.catalog-stub__title'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h4.catalog-stub__title').text
