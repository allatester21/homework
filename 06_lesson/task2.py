from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    # Ожидаем появления поля ввода и вводим текст "SkyPro"
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#newButtonName'))
    )
    input_field.send_keys('SkyPro')

    # Нажимаем на синюю кнопку
    submit_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
    submit_button.click()

    # Получаем новый текст кнопки
    updated_button_text = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'), 'SkyPro')
    )
    updated_button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

    print(updated_button_text)

finally:
    driver.quit()
