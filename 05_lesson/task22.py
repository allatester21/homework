from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Шаг 1: Открываем страницу
driver = webdriver.Firefox()  # Используем браузер Firefox
driver.get("http://the-internet.herokuapp.com/inputs")

# Шаг 2: Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Шаг 3: Вводим текст 1000
input_field.send_keys("1000")
time.sleep(0.5)  # Пауза, чтобы увидеть результат

# Шаг 4: Очищаем поле (методом clear)
input_field.clear()
time.sleep(0.5)  # Пауза, чтобы увидеть результат

# Шаг 5: Вводим текст 999
input_field.send_keys("999")

# Шаг 6: Закрываем браузер
time.sleep(5)  # Пауза перед закрытием, чтобы увидеть результат
driver.quit()
