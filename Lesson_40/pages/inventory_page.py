import time
import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class InventoryPage(BasePage):
    # Локаторы для элементов на странице Inventory
    HEADER_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ALL_ADD_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def is_header_visible(self):
        return self.is_visible(self.HEADER_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)
        return self

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def get_all_carts(self):
        return self.find_all(self.ALL_ADD_BUTTONS)

    @allure.step('Получаем список названий всех товаров в каталоге')
    def get_all_items_names(self):
        return self.get_all_texts(self.ITEM_NAMES)

    @allure.step('Добавление ВСЕХ доступных товаров в корзину')
    def add_all_items_to_cart(self):
        count = len(self.find_all(self.ALL_ADD_BUTTONS))

        for _ in range(count):
            buttons = self.find_all(self.ALL_ADD_BUTTONS)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[0])
            buttons[0].click()
            time.sleep(0.5)

        return self

    @allure.step('Переход в корзину')
    def go_to_cart(self):
        self.click(self.CART_ICON)
        return CartPage(self.driver)