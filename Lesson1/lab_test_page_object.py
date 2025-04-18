from pydoc import browse
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from MainPage import MainPage

def test_cart_counter():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('java')

