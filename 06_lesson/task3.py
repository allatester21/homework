from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

try:

    # Ждём загрузки всех изображений
    images = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'landscape'))
    )

    # Создаем массив элементов с тегом img
    image_array = driver.find_elements(By.TAG_NAME, 'img')
    img_count = len(image_array)
    print("Найдено изображений", img_count)

    # Получаем значение атрибута src у третьей картинки
    third_image_src = image_array[2].get_attribute('src')

    # Выводим значение в консоль
    print(f"Значение атрибута src 3-го изображения: {third_image_src}")

finally:
    driver.quit()
