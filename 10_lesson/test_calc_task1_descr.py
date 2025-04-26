from selenium import webdriver
from calc_page_object_descr import Calculator
import allure


@allure.suite("Тестирование сложения")
@allure.title("Тестирование калькулятора: {num1} + {num2} "
              "= {expected_result}")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "на сложение чисел.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_form():
    """
    Тест проверяет работу калькулятора с операцией сложения.
    :param browser: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+).
    :param num2: str — второе число для операции.
    :param result_field: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    browser = webdriver.Chrome()

    try:
        calculator = Calculator(browser)
        calculator.set_delay(4)
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')
        result_field = calculator.wait_result_field(6)
        assert result_field.text == '15', \
            f"Ожидался результат '15', но отобразился '{result_field.text}'"

        print("Тест успешно пройден: результат '15' отобразился после задержки.")

    finally:
        """
        Завершение работы драйвера
        """
        browser.quit()
