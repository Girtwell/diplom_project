import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.SearchApi import SearchApi
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")
        browser = None

        if browser_name == 'chrome':
            browser = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> SearchApi:

    url = ConfigProvider().get("api", "base_url")

    return SearchApi(url, 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTkyMjgxOTMsImlhdCI6MTc1OTA2MDE5MywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImZiOGY0NDg1NzE4NDY2MTk2MThmYzdlZThlNTYxZGQ1YWQ3ZTAzNmUzYTU2MWIxOTBjZmY0OGNkNTVhZTMxNTgiLCJ0eXBlIjoxMH0.zCzXnBdk_K-KpAYC5dvlJ_rmFxt0I0-OklAHkpXL1GE')
