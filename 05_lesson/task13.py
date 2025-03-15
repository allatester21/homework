from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Шаг 1: Открываем страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Шаг 2: Кликаем на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

# Шаг 3: Закрываем браузер
time.sleep(5)  # Пауза перед закрытием, чтобы увидеть результат
driver.quit()
