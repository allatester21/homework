# homework. Документация проекта.

## Описание базового синтаксиса записи и форматирования

Проект использует следующие технологии и синтаксис:

1. **Python**: Основной язык программирования для написания тестов.
2. **Selenium**: Библиотека для автоматизации взаимодействия с веб-браузером.
3. **Pytest**: Фреймворк для написания и запуска тестов.
4. **Allure**: Инструмент для генерации отчетов о выполнении тестов.

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

---

## Инструкция по запуску тестов для формирования отчета Allure

1. Установите необходимые зависимости:
   ```bash
   pip install allure-pytest
   ```

2. Запустите тесты с генерацией отчета Allure:
   ```bash
   pytest --alluredir allure-results
   ```

   Эта команда запустит все тесты и сохранит результаты в директорию `allure-results`.

---

## Инструкция по просмотру сформированного отчета Allure

1. После завершения тестов, чтобы просмотреть отчет, выполните команду:
   ```bash
   allure serve allure-result
   ```

   Эта команда запустит локальный сервер и откроет отчет в браузере.

2. В отчете Allure вы увидите:
   1. Тестирование калькулятора
         - **Название теста**: `Тестирование калькулятора: 7 + 8 = 15`.
         - **Описание теста**: Тест проверяет корректность работы калькулятора на сложение чисел.
         - **Шаги теста**:
           - Открытие страницы калькулятора.
           - Установка задержки.
           - Нажатие кнопок.
           - Ожидание результата.
           - Проверка результата.
         - **Результат**: Успешное выполнение или ошибка с указанием ожидаемого и фактического результата.
   2. Тестирование магазина
         - **Название теста**: `Тестирование магазина`
         - **Описание теста**: Тест проверяет корректность работы магазина.
         - **Шаги теста**:
           - Открытие страницы авторизации магазина.
           - Введение данных пользователя.
           - Переход на страницу товаров.
           - Ожидание загрузки страницы товаров.
           - Добавление товаров.
           - Переход в корзину.
           - Ожидание загрузки корзины.
           - Переход на страницу заполнения формы.
           - Ожидание загрузки страницы.
           - Заполнение формы.
           - Нажатие на кнопку "Continue".
           - Ожидание загрузки страницы.
           - Сравнение итоговой суммы покупки.
           - Проверка результата.
         - **Результат**: Успешное выполнение или ошибка с указанием ожидаемого и фактического результата.
