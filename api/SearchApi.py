import allure
import requests
from urllib.parse import quote


@allure.epic("Работа с API")
class SearchApi:
    """
    Этот класс представляет сущность "Хелперы по работе с API".
    """
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

    @allure.step("Поисковая строка")
    def search(self, title: str) -> dict:
        """
        Отправляет запрос для поисковой строки и возвращает результат
        """
        encoded_title = quote(title)
        path = f"{self.base_url}/search/facet-search?customerCityId=213&phrase={encoded_title}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.chitai-gorod.ru/',
            'Origin': 'https://www.chitai-gorod.ru',
            'Authorization': self.token
        }
        with allure.step("Отправить GET запрос с {title}"):
            resp = requests.get(path, headers=headers)
        with allure.step("Получить ответ"):
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"Ошибка запроса: {resp.status_code}")
                print(f"Текст ответа: {resp.text}")
                return {"error": resp.status_code, "message": resp.text}
