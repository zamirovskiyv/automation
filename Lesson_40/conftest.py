import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    # prefs = {
    #     "credentials_enable_service": False,  # Отключаем предложение сохранить пароль
    #     "profile.password_manager_enabled": False,  # Отключаем сам менеджер паролей
    #     "profile.password_manager_leak_detection": False,  # Отключаем проверку утечек паролей
    #     "safebrowsing.enabled": False  # Отключаем антивирус (Safe Browsing)
    # }
    #
    # options.add_experimental_option("prefs", prefs)

    options.add_argument("--headless=new")  # Режим без визуального отображения браузера
    options.add_argument("--window-size=1920,1080")  # Установка размера окна для корректной работы в headless режиме

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=service, options=options)

    yield my_driver

    my_driver.quit()
