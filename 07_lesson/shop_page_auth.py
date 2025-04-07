from selenium.webdriver.common.by import By
import time


class Authorization():

    def __init__(self, driver):
        # Инициализируем драйвер браузера
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def input_auth(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(2)
        login_button.click()
