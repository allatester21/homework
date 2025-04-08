from selenium import webdriver
from calc_page_object import Calculator


def test_calculator_form():
    browser = webdriver.Chrome()

    try:
        calculator = Calculator(browser)
        calculator.set_delay(45)
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')
        result_field = calculator.wait_result_field(50)
        assert result_field.text == '15', \
            f"Ожидался результат '15', но отобразился '{result_field.text}'"

        print("Тест успешно пройден: результат '15' отобразился после задержки.")

    finally:
        browser.quit()
