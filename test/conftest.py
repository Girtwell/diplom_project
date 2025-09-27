import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api.SearchApi import SearchApi


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> SearchApi:
    return SearchApi("https://web-gate.chitai-gorod.ru/api/v2", 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTkxNjM5NjIsImlhdCI6MTc1ODk5NTk2MiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjQ3ZDdkNzcwNDI3MGNlZDY3MmNkYTliNjljNjI3NzBkYzhhZGRkNDBlN2Q5N2I3YWQ5N2VmNzFkZDcxOGQ2YzUiLCJ0eXBlIjoxMH0.e3hZymLqlZEp_h9uziWxD4X7DT6coeSjyqfJr6BE6Rg')
