from pydoc import browse
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

browser = webdriver.Chrome()

# Перейти на сайт Лабиринта
def open_labirint():
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(2)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    # Добавить все книги в корзину и посчитать сколько
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверить счетчик товаров, должен соответствовать количеству добавленных книг
    # Получаем текущее значение:
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    return int(txt.split()[0])

def close_driver():
    browser.quit()

def test_cart_counter():
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter    # Сравниваем с counter

#def test_empty_search():
#    open_labirint()
#    search('0000000000')
#    txt = browser.find_element(By.CSS_SELECTOR, 'h1').text
#    assert txt == 'Все, что мы нашли в Лабиринте по запросу'
#    close_driver()
