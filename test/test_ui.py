from page.MainPage import MainPage
from page.CartPage import CartPage


def test_book_search_pozitive(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search("Стивен Кинг Сияние")
    res = main_page.correct_result_search()
    assert res == 'Результаты поиска «стивен кинг сияние»'


def test_book_search_negative(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search("xzxtgxdt123!@#")
    res = main_page.not_correct_result_search()
    assert res == 'Похоже, у нас такого нет'


def test_dropdown_list(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    title = main_page.dropdown_list()
    assert title == 'Популярные запросы'


def test_add_book_to_cart(browser):
    cart_page = CartPage(browser)
    cart_page.go_cart()

    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search("Стивен Кинг Сияние")
    main_page.choose_book()
    main_page.button_by()

    cart_page = CartPage(browser)
    cart_page.go_cart()
    item = cart_page.item_in_cart()
    assert item == '1 товар'


def test_clear_cart(browser):
    cart_page = CartPage(browser)
    cart_page.go_cart()

    main_page = MainPage(browser)
    main_page.go()
    main_page.click_search_field()
    main_page.book_search("Стивен Кинг Сияние")
    main_page.choose_book()
    main_page.button_by()

    cart_page = CartPage(browser)
    cart_page.go_cart()
    cart_page.clear_cart()
    message = cart_page.message_clear_cart()
    assert message == 'Корзина очищена'
