from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    @allure.step("Открытие страницы калькулятора")
    def __init__(self, driver):
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки в секундах '{delay}'")
    def set_delay(self, delay) -> int:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param delay: int — время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, 'delay')  # Вводим значение задержки
        delay_input.clear()  # Очищаем поле, если там есть значение
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}'")
    def click_button(self, button) -> str:
        """
        Нажимает на кнопку калькулятора
        :param button: str текст на кнопке которую нужно нажать
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Ожидание результата '{timeout}'")
    def wait_result_field(self, timeout) -> int:
        """
        Время ожидания отображения результата на экране калькулятора
        :param timeout: int время задержки в секундах
        """
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.invisibility_of_element_located((By.ID, 'spinner')))

        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str - текст на экране калькулятора
        """
        result_field = self.driver.find_element(By.CLASS_NAME, 'screen')
        return result_field
