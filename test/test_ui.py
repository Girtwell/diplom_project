import allure
from page.MainPage import MainPage
from page.CartPage import CartPage


@allure.title("Найти книгу по корректному запросу через поле поиска")
@allure.description("Тест проверяет, что выводится результат по запросу")
def test_book_search_pozitive(browser, test_data: dict):
    title = test_data.get("title_lat")
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search(title)
    res = main_page.correct_result_search()

    with allure.step("Проверить, что вышлел резутат по запросу: "+res):
        assert res == 'Результаты поиска «fairy tales»'


@allure.title("Найти книгу по некорректному запросу через поле поиска")
@allure.description(
    "Тест проверяет, что при не корректном запросе выводится сообщение")
def test_book_search_negative(browser, test_data: dict):
    title_non_correct = test_data.get("title_non_correct")
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search(title_non_correct)
    message = main_page.not_correct_result_search()
    with allure.step("Проверить, что вышло сообщение: " + message):
        assert message == 'Похоже, у нас такого нет'


@allure.title(
        "Заголовок 'Популярные запросы' отображается в выпадающем списке")
@allure.description(
    "Тест проверяет, что выпадающем списке есть заголовок: Популярные запросы")
def test_dropdown_list(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    title = main_page.dropdown_list()
    with allure.step(
            "Проверить, что в выпадающем списке есть заголовок: "+title):
        assert title == 'Популярные запросы'


@allure.title("Добавление товара в корзину")
@allure.description("Тест проверяет, что товар добавлен в корзину")
def test_add_book_to_cart(browser, test_data: dict):
    title = test_data.get("title_lat")
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search(title)
    main_page.choose_book()
    main_page.button_by()

    cart_page = CartPage(browser)
    cart_page.go_cart()
    item = cart_page.item_in_cart()

    with allure.step("Проверить, что товар добавлен в корзине: " + item):
        assert item == '1 товар'


@allure.title("Удаление товара из корзины")
@allure.description(
    "Тест проверяет, что выводится сообщение при очистке корзины")
def test_clear_cart(browser, test_data: dict):
    title = test_data.get("title_lat")
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search(title)
    main_page.choose_book()
    main_page.button_by()

    cart_page = CartPage(browser)
    cart_page.go_cart()
    cart_page.clear_cart()
    message = cart_page.message_clear_cart()
    with allure.step("Проверить, что появилось сообщение: " + message):
        assert message == 'Корзина очищена'
