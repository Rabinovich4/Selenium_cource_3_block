import time
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_any_lang_find_btn_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)

    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"), "Кнопка не найдена"

