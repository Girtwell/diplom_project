import allure
import requests
from urllib.parse import quote
from typing import Optional, Dict


@allure.epic("Работа с API")
class SearchApi:
    """
    Этот класс представляет сущность "Хелперы по работе с API".
    """
    def __init__(self, base_url: str, token: Optional[str] = None) -> None:
        self.base_url = base_url
        self.token = token

    def _get_headers(self, auth_required: bool = True) -> Dict[str, str]:
        """
        Возвращает полный набор заголовков для имитации
        современного браузера Chrome. Основан на реальных заголовках
        из браузера для максимальной достоверности.

        Args:
            auth_required: Нужно ли включать заголовок авторизации

        Returns:
            Dict с заголовками браузера
        """
        headers = {
            # Основные заголовки браузера
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',

            # Современные заголовки безопасности Chrome
            'Sec-Ch-Ua': '"Chromium";v="140", "Not A?Brand";v="24", "Google Chrome";v="140"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',

            # Заголовки соединения и приватности
            'Connection': 'keep-alive',
            'DNT': '1',

            # Заголовки сайта
            'Referer': 'https://www.chitai-gorod.ru/',
            'Origin': 'https://www.chitai-gorod.ru',
        }

        # Добавляем авторизацию если нужно и токен есть
        if auth_required and self.token:
            headers['Authorization'] = self.token

        return headers

    @allure.step("Поисковая строка")
    def search(self, title: str) -> dict:
        """
        Отправляет запрос для поисковой строки и возвращает результат
        Args:
            title: Поисковая фраза
        Returns:
            Dict с результатами поиска или ошибкой
        """
        # Правильное кодирование для кириллицы и других Unicode символов
        encoded_title = quote(title, encoding='utf-8', safe='')
        path = f"{self.base_url}/search/facet-search?customerCityId=213&phrase={encoded_title}"

        headers = self._get_headers()

        with allure.step(f"Отправить GET запрос с '{title}' (закодировано как: {encoded_title})"):
            resp = requests.get(path, headers=headers, timeout=30)

        with allure.step("Получить ответ"):
            if resp.status_code == 200:
                # Убеждаемся, что кодировка ответа правильная для кириллицы
                resp.encoding = resp.apparent_encoding or 'utf-8'
                return resp.json()
            else:
                print(f"Ошибка запроса: {resp.status_code}")
                resp.encoding = resp.apparent_encoding or 'utf-8'
                print(f"Текст ответа: {resp.text}")
                return {"error": resp.status_code, "message": resp.text}

    @allure.step("Получение информации о товаре")
    def get_product(self, product_id: str) -> dict:
        """
        Получает информацию о конкретном товаре
        Args:
            product_id: ID товара
        Returns:
            Dict с информацией о товаре или ошибкой
        """
        path = f"{self.base_url}/product/{product_id}"
        headers = self._get_headers()

        with allure.step(f"Отправить GET запрос для товара {product_id}"):
            resp = requests.get(path, headers=headers, timeout=30)

        with allure.step("Получить ответ"):
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"Ошибка запроса: {resp.status_code}")
                print(f"Текст ответа: {resp.text}")
                return {"error": resp.status_code, "message": resp.text}
