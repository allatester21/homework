from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Шаг 1: Открываем страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Шаг 2: Кликаем на кнопку
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

# Шаг 3: Закрываем браузер
time.sleep(5)  # Пауза перед закрытием, чтобы увидеть результат
driver.quit()
