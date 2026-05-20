from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage

class LoginPage(BasePage):
    # Локаторы для элементов на странице Login
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def open_page(self):
        self.open("https://www.saucedemo.com/")
        return self

    def login_success(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

        return InventoryPage(self.driver)

    def login_fail(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

        return self
