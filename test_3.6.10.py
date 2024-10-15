import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_button_text = {
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier',
}

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_for_changing_the_language_of_the_add_to_cart_button(browser, user_language):
    # Arrange
    browser.get(link)
    # Act
    button_add_to_cart = browser.find_element(By.XPATH, '//*[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    print('В терминале был установлен язык', user_language, 'и на кнопке была надпись', button_add_to_cart.text)
    # Assert
    assert button_add_to_cart.text in expected_button_text[user_language], 'Неверное содержание текста кнопки'


# Запуск теста из терминала:
# pytest --language=es review3.6.10/test_3.6.10.py -s -v
# pytest -s -v --language=fr review3.6.10/test_3.6.10.py

