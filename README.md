# diplom_project
Tests: API, UI

## Автоиматизация тестов API, UI на python

### Шаги:
1. Склонировать проект `git clone https://github.com/Girtwell/diplom_project.git`
2. Установить все зависимости `pip install > -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- webdriver manager
- request 
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы по работе с API
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json
