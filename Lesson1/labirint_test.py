from time import sleep
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter():
    browser = webdriver.Chrome()

    # Перейти на сайт Лабиринта
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(2)
    browser.maximize_window()
    browser.add_cookie(cookie)

    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # Добавить все книги в корзину и посчитать сколько
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    print((counter))
    sleep((1))

    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров, должен соответствовать количеству добавленных книг
    # Получаем текущее значение:
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    print(txt)

    # Сравниваем с counter
    assert counter == int(txt.split()[0])

    browser.quit()
