import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider


@allure.epic("Главная страница")
class MainPage:
    """
    Этот класс представляет сущность "Главная страница".
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор инициализирует браузер.
        """
        url = ConfigProvider().get("ui", "base_url")
        self.__url = url
        self.__driver = driver

    @allure.step("Открыть главную страницу")
    def go(self) -> None:
        """
        Открывает главную страницу
        """
        self.__driver.get(self.__url)

    @allure.step("Нажать на поле поиска")
    def click_search_field(self) -> None:
        """
        Находит поле "Поиск", нажимает на него.
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').click()

    @allure.step("Ввести запрос {book_title} в поле поиска")
    def book_search(self, book_title: str) -> None:
        """
        Вводит значение в поле поиск.
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').send_keys(book_title)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Найти"]').click()

    @allure.step("Дождаться появления выпадающий список")
    def dropdown_list(self) -> None:
        """
        Ждет пока появится выпадающий список.
        Возвращает заголовок выпадающего списка.
        """
        (WebDriverWait(
            self.__driver, 15).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'span.suggests-list__header'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'span.suggests-list__header').text

    @allure.step("Дождаться результат поиска корректного запроса")
    def correct_result_search(self) -> str:
        """
        Ждет пока появится сообщение результата поиска запроса,
        возвращает текст сообщения.
        """
        (WebDriverWait(
            self.__driver, 15).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h1.search-title__head'))))

        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.search-title__head').text

    @allure.step("Дождаться результат поиска некорректного запроса")
    def not_correct_result_search(self) -> str:
        """
        Ждет пока появится сообщение результата поиска запроса,
        возвращает текст сообщения.
        """
        (WebDriverWait(
            self.__driver, 15).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h4.catalog-stub__title'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h4.catalog-stub__title').text

    @allure.step("Нажать на выбраную книгу")
    def choose_book(self) -> None:
        """
        Ждет пока отобразится книга.
        Нажимает выбранную книгу.
        """
        (WebDriverWait(
            self.__driver, 15).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'a[href="/product/fairy-tales-3024828"]'
                    ))))
        self.__driver.find_element(
            By.CSS_SELECTOR, 'a[href="/product/fairy-tales-3024828"]').click()

    @allure.step("Нажать на кнопку 'Купить'")
    def button_by(self) -> None:
        """
        Ждет пока появится кнопка купить.
        Нажимает кнопку купить.
        """
        (WebDriverWait(
            self.__driver, 15).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'button[aria-label="false"]'))))
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="false"]').click()
