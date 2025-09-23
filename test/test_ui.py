from page.MainPage import MainPage
import time


def test_book_search_pozitive(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.book_search("Стивен Кинг Сияние")
    res = main_page.result_search()
    assert res == 'Результаты поиска «стивен кинг сияние»'
    time.sleep(5)


def test_book_search_negative(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.book_search("xzxtgxdt123!@#")
    res = main_page.message_result_search()
    assert res == 'Похоже, у нас такого нет'
