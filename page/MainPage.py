from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Этот класс представляет сущность "Главная страница".
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор инициализирует браузер.
        """
        self.__url = "https://www.chitai-gorod.ru"
        self.__driver = driver

    def go(self) -> None:
        """
        Открывает главную страницу
        """
        self.__driver.get(self.__url)

    def click_search_field(self):
        """
        Находит поле "Поиск", нажимает на него.
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').click()

    def book_search(self, book_title: str) -> None:
        """
        Вводит значение в поле поиск.
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="search"]').send_keys(book_title)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Найти"]').click()

    def dropdown_list(self) -> None:
        """
        Ждет пока появится выпадающий список.
        Возвращает заголовок выпадающего списка.
        """
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'span.suggests-list__header'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'span.suggests-list__header').text

    def correct_result_search(self) -> str:
        """
        Ждет пока появится сообщение результата поиска запроса,
        возвращает текст сообщения.
        """
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h1.search-title__head'))))

        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.search-title__head').text

    def not_correct_result_search(self) -> str:
        """
        Ждет пока появится сообщение результата поиска запроса,
        возвращает текст сообщения.
        """
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'h4.catalog-stub__title'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'h4.catalog-stub__title').text

    def choose_book(self) -> None:
        """
        Ждет пока отобразится книга.
        Нажимает выбранную книгу.
        """
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'a[href="/product/siyanie-2827510"]'))))
        self.__driver.find_element(
            By.CSS_SELECTOR, 'a[href="/product/siyanie-2827510"]').click()

    def button_by(self) -> None:
        """
        Ждет пока появится кнопка купить.
        Нажимает кнопку купить.
        """
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'button[aria-label="false"]'))))
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="false"]').click()
