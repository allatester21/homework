from selenium.webdriver.common.by import By
import allure


class Authorization:
    """
    Класс для авторизации пользователя в магазине.
    Вносит логин и пароль пользователя
    """

    @allure.step("Открытие страницы авторизации магазина")
    def __init__(self, driver):
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Введение данных пользователя")
    def input_auth(self, username: str, password: str) -> str:
        """
        Вносит данные пользователя в поля формы
        :param username: str имя пользователя
        :param password: str пароль пользователя
        """
        with allure.step(f"Вносит имя пользователя '{username}'"):
            username_field = self.driver.find_element(By.ID, "user-name")

        with allure.step(f"Вносит пароль пользователя '{password}'"):
            password_field = self.driver.find_element(By.ID, "password")

        with allure.step("Нажимаем кнопку Login"):
            login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
