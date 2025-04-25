from selenium import webdriver
from shop_page_auth_descr import Authorization
from shop_page_select_descr import Product
from shop_page_checkout_descr import Checkout
from shop_page_form_descr import Form
import allure


@allure.suite("Тестирование магазина")
@allure.title("Тестирование покупок в магазине")
@allure.description("Тест проверяет корректность работы магазина: авторизация пользователя, добавление товаров "
                    "в корзину, проверка списка товаров в корзине, заполнение инфо по доставке "
                    "и сверка общей суммы товаров в корзине.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    browser = webdriver.Chrome()
    auth = Authorization(browser)
    auth.input_auth("standard_user", "secret_sauce")

    product = Product(browser)
    product.wait_load(10, "inventory_item")  # Ожидание загрузки страницы с товарами

    product.select_item('add-to-cart-sauce-labs-backpack')
    product.select_item('add-to-cart-sauce-labs-bolt-t-shirt')
    product.select_item('add-to-cart-sauce-labs-onesie')

    product.cart("shopping_cart_link")
    product.wait_load(10, "cart_item")   # Ожидание загрузки страницы корзины

    checkout = Checkout(browser)
    checkout.button("checkout")

    form = Form(browser)
    form.wait_load_id(10, "first-name")  # Ожидание загрузки страницы формы
    form.fill_form("first-name", "Alla")
    form.fill_form("last-name", "Ladygina")
    form.fill_form("postal-code", "650056")

    form.click_form("continue")

    product.wait_load(10, "summary_info")  # Ожидание загрузки страницы Overview
    total_value = form.overview("summary_total_label")

    """
    Проверка итоговой суммы
    """
    expected_total = 58.29
    assert total_value == expected_total, \
        (f"Итоговая сумма составляет ${total_value:.2f}, "
         f"ожидалось ${expected_total:.2f}")

    print(f"Проверка пройдена: итоговая сумма составляет ${total_value:.2f}")

    browser.quit()
