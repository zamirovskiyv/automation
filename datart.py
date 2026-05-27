# Импортируем нужные модули для работы с браузером и веб-элементами
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def create_driver():
    # Опции браузера
    options = webdriver.ChromeOptions()
    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )  # Отключение автоматического определения бот-активности
    # options.add_argument("--start-maximized")  # Запуск браузера в полноэкранном режиме
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def search_keyword(keyword):
    driver = create_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(url="https://www.datart.cz/")

        # Согласие с куки иногда появляется позже, поэтому используем ограниченное ожидание.
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn")))
            cookie_button.click()
        except TimeoutException:
            pass

        search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']")))
        search_input.send_keys(keyword)  # Вводим ключевое слово в поисковую строку
        search_input.send_keys(Keys.ENTER)  # Нажимаем клавишу Enter для выполнения поиска

        # Дожидаемся, что страница результатов отрисовалась (или есть карточки товара).
        wait.until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Výsledky') or contains(., 'výsledky')]")),
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'col-md-6') and contains(@class, 'col-xl-4')]")),
            )
        )
        print(f"Выполнен поиск по ключевому слову: '{keyword}'")
        products = driver.find_elements(By.XPATH, "//div[@class='col-md-6 col-xl-4']")
        count = 0  # Счетчик товаров, содержащих заданное слово

        for product in products:
            title = product.find_element(By.XPATH, ".//h3[@class='item-title']")  # Название товара
            description = product.find_element(By.XPATH, ".//div[@class='item-description']")  # Описание товара

            #     iPhone == Iphone
            if keyword.lower() in title.text.lower() or keyword.lower() in description.text.lower():
                count += 1

        time.sleep(6)
        if count >= 2:
            print(f"Проверка пройдена: найдено {count} упоминаний ключевого слова '{keyword}'.")
        else:
            print("Проверка не пройдена.")
        time.sleep(4)
    finally:
        print("Закрываю браузер...")
        driver.quit()


if __name__ == "__main__":
    search_keyword("mavic")
