# Путь для запуска:
# pytest --language=es test_items.py


import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



def test_launching_autotests_for_different_languages(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    wait = WebDriverWait(browser, 5)
    button_text = wait.until(
        ec.visibility_of_element_located((
            By.CSS_SELECTOR,
            "button.btn.btn-lg.btn-primary.btn-add-to-basket"
        ))
    ).text

    assert button_text is not None, "Страница товара на сайте не содержит кнопку добавления в корзину"

