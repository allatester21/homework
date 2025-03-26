from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер браузера
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

try:

    # Вводим значение задержки
    delay_input = driver.find_element(By.ID, 'delay')
    delay_input.clear()  # Очищаем поле, если там есть значение
    delay_input.send_keys('45')

    # Нажимаем кнопки
    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    # Ожидаем появления результата в течение указанной задержки
    waiter = WebDriverWait(driver, 50).until(
        EC.invisibility_of_element_located((By.ID, 'spinner')))

    result_field = driver.find_element(By.CLASS_NAME, 'screen')

    # Проверяем, что отобразился правильный результат
    assert result_field.text == '15', \
        f"Ожидался результат '15', но отобразился '{result_field.text}'"

    print("Тест успешно пройден: результат '15' отобразился после задержки.")

finally:
    # Закрываем браузер
    driver.quit()
