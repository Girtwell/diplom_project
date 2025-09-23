from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Этот класс представляет сущность "Корзина".
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор инициализирует браузер.
        """
        self.__url = "https://www.chitai-gorod.ru"
        self.__driver = driver

    def go_cart(self):
        """
        Открывает страницу корзины.
        """
        self.__driver.get(self.__url + "/cart")

    def item_in_cart(self):
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'span.cart-page__title--append'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'span.cart-page__title--append').text

    def clear_cart(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, 'span.cart-page__clear-cart-title').click()

    def message_clear_cart(self):
        (WebDriverWait(
            self.__driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'p.cart-multiple-delete__title'))))
        return self.__driver.find_element(
            By.CSS_SELECTOR, 'p.cart-multiple-delete__title').text
