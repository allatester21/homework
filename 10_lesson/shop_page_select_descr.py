from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Product:
    """
    Класс для добавления товара в корзину
    """

    @allure.step("Переходим на страницу с товарами")
    def __init__(self, driver):
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ожидание загрузки страницы")
    def wait_load(self, timeout: int, element) -> None:

        WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, element)))

    @allure.step("Добавление товара '{item_id}' в корзину")
    def select_item(self, item_id: str) -> str:
        """
        Добавляем в корзину товары
        :param item_id: str наименование товара
        """
        self.driver.find_element(By.ID, item_id).click()

    @allure.step("Переходим в корзину")
    def cart(self, item_class: str) -> str:
        """
        Переходим в корзину
        :param item_class: str обозначение корзины
        """
        self.driver.find_element(By.CLASS_NAME, item_class).click()
