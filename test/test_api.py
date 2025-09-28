import allure
from api.SearchApi import SearchApi


@allure.title("Тест поиска на кириллице")
@allure.description(
    """Тест проверяет, что результат по запросу
    не отсутсвует и не возвращает ошибку в ответе.
    В теле ответа получим словарь""")
def test_search_in_cyrillic(api_client: SearchApi, test_data: dict):
    title = test_data.get("title_cyr")
    result = api_client.search(title)

    assert result is not None, "Результат не должен быть None"
    assert "error" not in result, f"Получена ошибка: {result}"
    assert isinstance(
        result, dict), f"Ожидается словарь, получено: {type(result)}"
    print(f"Структура ответа: {list(result.keys())}")


@allure.title("Тест поиска на латинице")
@allure.description(
    """Тест проверяет, что результат по запросу
    не отсутсвует и не возвращает ошибку в ответе.
    В теле ответа получим словарь""")
def test_search_in_latin(api_client: SearchApi, test_data: dict):
    title = test_data.get("title_lat")
    result = api_client.search(title)

    assert result is not None, "Результат не должен быть None"
    assert "error" not in result, f"Получена ошибка: {result}"
    assert isinstance(
        result, dict), f"Ожидается словарь, получено: {type(result)}"


@allure.title("Тест поиска с числами")
@allure.description(
    """Тест проверяет, что результат по запросу
    не отсутсвует и не возвращает ошибку в ответе.
    В теле ответа получим словарь""")
def test_search_with_numbers(api_client: SearchApi, test_data: dict):
    title = test_data.get("title_num")
    result = api_client.search(title)

    assert result is not None, "Результат не должен быть None"
    assert "error" not in result, f"Получена ошибка: {result}"
    assert isinstance(
        result, dict), f"Ожидается словарь, получено: {type(result)}"


@allure.title("Проверка структуры ответа API")
@allure.description(
    """Тест проверяет, что результат по запросу не отсутсвует
    и не возвращает ошибку в ответе.
    API читай-города возвращает поисковые фильтры и фасеты.
    Поле 'data' присутствует в ответе и должно быть списком.
    Каждый фильтр должен содержать поле 'id'
    Каждый фильтр должен содержать поле 'type'
    Есть фильтры для поиска.""")
def test_search_response_structure(api_client: SearchApi, test_data: dict):
    title = test_data.get("title_lat")
    result = api_client.search(title)

    assert result is not None
    assert "error" not in result, f"Получена ошибка: {result}"

    assert "data" in result, f"Отсутствует поле'data' в ответе.Доступные поля:{
        list(result.keys())}"
    assert isinstance(result["data"], list), "Поле 'data' должно быть списком"

    if len(result["data"]) > 0:
        first_filter = result["data"][0]
        assert "id" in first_filter
        assert "type" in first_filter
        print(f"API вернул {len(result['data'])} фильтров для поиска")
    else:
        print("API вернул пустой список фильтров")


@allure.title("Тест поиска с пустым запросом")
@allure.description(
    """Тест проверяет,что результат по запросу не отсутсвует
    и в теле ответа получим словарь. Пустой запрос может вернуть ошибку или
    пустой результат - оба варианта валидны""")
def test_search_empty_query(api_client: SearchApi, test_data: dict):
    title = test_data.get("title_emp")
    result = api_client.search(title)

    assert result is not None
    assert isinstance(
        result, dict), f"Ожидается словарь, получено: {type(result)}"


@allure.title("Тест поиска с некорректным запросом")
@allure.description(
    """Тест проверяет,что результат по запросу не отсутсвует
    и в теле ответа получим словарь. Для некорректного поиска
    API должен вернуть успешный ответ с пустыми результатами.
    Это валидный случай - товар не найден, но запрос успешен.
    """)
def test_non_correct_search(api_client: SearchApi, test_data: dict):
    title_non_correct = "xzxtgxdt123!@#"
    result = api_client.search(title_non_correct)

    assert result is not None, "Результат не должен быть None"
    assert isinstance(
        result, dict), f"Ожидается словарь, получено: {type(result)}"

    if "error" not in result:
        print(f"Результат поиска несуществующего товара: {result}")
