import pytest
import allure
from ..pages.login_page import LoginPage

@allure.feature("Интернет-магазин Swag Labs")
@allure.story("Покупка товаров")
@allure.title("Успешный вход и добавление товара в корзину")
def test_buy_backpack(driver):

    login_page = LoginPage(driver).open_page()

    inventory_page = login_page.login_success("standard_user", "secret_sauce")

    assert inventory_page.is_header_visible() == True, "Баг: Мы не попали в каталог!"

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1", "Баг: Товар не добавился в корзину!"

@allure.feature("Интернет-магазин Swag Labs")
@allure.story("Покупка товаров")
@allure.title("Массовое добавление всех товаров в корзину")
def test_buy_all_items(driver):
    login_page = LoginPage(driver).open_page()

    inventory_page = login_page.login_success("standard_user", "secret_sauce")

    all_count = len(inventory_page.get_all_carts())
    inventory_page.add_all_items_to_cart()

    assert int(inventory_page.get_cart_count()) == all_count, "Баг: Не все товары добавились в корзину!"


@allure.feature("Интернет-магазин Swag Labs")
@allure.story("Корзина")
@allure.title("Проверка целостности данных: Каталог -> Корзина")
def test_cart_items_match(driver):
    login_page = LoginPage(driver).open_page()
    inventory_page = login_page.login_success("standard_user", "secret_sauce")

    expected_names = inventory_page.get_all_items_names()
    inventory_page.add_all_items_to_cart()
    cart_page = inventory_page.go_to_cart()

    actual_names = cart_page.get_cart_items_names()

    with allure.step('Сверяем списки товаров'):
        assert expected_names == actual_names, "Баг: Названия товаров в корзине не совпадают с каталогом!"