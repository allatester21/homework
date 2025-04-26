from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Form:
    """
    Класс для заполнения формы информации о пользователе
    """

    @allure.step("Переходим на страницу формы")
    def __init__(self, driver):
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ожидание загрузки страницы '{timeout}'")
    def wait_load_id(self, timeout: int, element: str):
        """
        Время ожидания загрузки страницы с формой
        :param timeout: int время задержки в секундах
        :param element: str появление поля "First Name"
        """
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located((By.ID, element)))

    @allure.step("Заполняем форму '{field}' значением '{value}'")
    def fill_form(self, field: str, value: str) -> str:
        """
        Заполнение полей
        :param field: str название поля
        :param value: str значение поля
        """
        self.driver.find_element(By.ID, field).send_keys(value)

    @allure.step("Нажать на кнопку Continue")
    def click_form(self, button: str) -> str:
        """
        Нажать на кнопку
        :param button: str название кнопки
        """
        self.driver.find_element(By.ID, button).click()

    @allure.step("Сравнение итоговой суммы покупки")
    def overview(self, item: str) -> str:
        """
        Сравнение суммы всех товаров с итоговой суммой
        :param item: float сумма покупки
        """
        with allure.step("Итоговая сумма"):
            total_element = self.driver.find_element(By.CLASS_NAME, item)

        with allure.step("Выбираем значение"):
            total_text = total_element.text

        with allure.step("Переводим значение из строковой в число с плавающей запятой"):
            total_value = float(total_text.split("$")[1])
        return total_value
