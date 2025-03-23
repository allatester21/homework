from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # Ждем появления синей кнопки и нажимаем её
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ajaxButton'))
    )
    button.click()

    # Ждем появления текста в зеленой плашке
    text_element = WebDriverWait(driver, 18).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
    )

    # Получаем текст из элемента
    text = text_element.text
    print(text)

finally:
    driver.quit()
