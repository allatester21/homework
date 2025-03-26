from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

try:
    # Ожидаем загрузки страницы и заполнения формы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'first-name')))

    # Заполняем форму
    driver.find_element(By.NAME, 'first-name').send_keys('Иван')
    driver.find_element(By.NAME, 'last-name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'city').send_keys('Москва')
    driver.find_element(By.NAME, 'country').send_keys('Россия')
    driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, 'job-position').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')

    # Нажимаем кнопку Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3')
    submit_button.click()

    # Проверяем, что поле Zip code подсвечено красным
    zip_code_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'zip-code')))

    zip_code_border_color = zip_code_field.value_of_css_property('border-color')
    assert zip_code_border_color == 'rgb(245, 194, 199)', \
    f'Поле Zip code подсвечено цветом: {zip_code_border_color}, ожидалось: rgb(245, 194, 199)'

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        'first-name',
        'last-name',
        'address',
        'city',
        'country',
        'e-mail',
        'phone',
        'job-position',
        'company'
    ]

    for field_id in fields_to_check:
        field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, field_id)))

        border_color = field.value_of_css_property('border-color')
        assert border_color == 'rgb(186, 219, 204)', \
            f'Поле {field_id} подсвечено цветом: {border_color}, ожидалось: rgb(186, 219, 204)'

    print("Тест успешно пройден: поле Zip code подсвечено красным,"
          "остальные поля - зеленым.")

finally:
    # Закрываем браузер
    driver.quit()
