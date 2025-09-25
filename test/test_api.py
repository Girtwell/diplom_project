from api.SearchApi import SearchApi


def test_search_in_сyrillic():
    api = SearchApi()
    title = "Сияние"
    api.search(title)


def test_search_in_latin():
    api = SearchApi()
    title = "The little prince"
    api.search(title)


def test_search_with_numbers():
    api = SearchApi()
    title = "1984"
    api.search(title)


def test_non_correct_search():
    api = SearchApi()
    title = "xzxtgxdt123!@#"
    api.search(title)
