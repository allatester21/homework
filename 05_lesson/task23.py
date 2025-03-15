from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Шаг 1: Открываем страницу
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Шаг 2: Находим поля ввода для имени пользователя и пароля
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Шаг 3: Вводим значения в поля
username_field.send_keys("tomsmith")
time.sleep(0.5)  # Пауза, чтобы увидеть результат
password_field.send_keys("SuperSecretPassword!")
time.sleep(0.5)  # Пауза, чтобы увидеть результат

# Шаг 4: Нажимаем кнопку Login
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()

# Шаг 5: Закрываем браузер
time.sleep(5)  # Пауза перед закрытием, чтобы увидеть результат
driver.quit()
