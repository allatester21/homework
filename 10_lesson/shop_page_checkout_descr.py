from selenium.webdriver.common.by import By
import allure


class Checkout:
    """
    Класс для проверки добавленных товаров в корзину
    """

    @allure.step("Переходим в корзину")
    def __init__(self, driver):
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Переходим на следующую страницу")
    def button(self, button_id: str) -> str:
        self.driver.find_element(By.ID, button_id).click()
