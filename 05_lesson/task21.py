from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Шаг 1: Открываем страницу
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Шаг 2: Ожидаем появления модального окна
time.sleep(3)  # Ждем 3 секунды для загрузки модального окна

# Шаг 3: Находим кнопку Close в модальном окне и кликаем на неё
close_button = driver.find_element(By.XPATH, "//p[text()='Close']")
close_button.click()

# Шаг 4: Закрываем браузер
time.sleep(5)  # Пауза перед закрытием, чтобы увидеть результат
driver.quit()
