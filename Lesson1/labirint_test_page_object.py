from pydoc import browse
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pades.MainPage import MainPage

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage();
    main_page.set_cookie_policy()
