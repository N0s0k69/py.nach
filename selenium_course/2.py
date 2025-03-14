from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Путь к файлу, который нужно загрузить
file_path = os.path.abspath("example.txt")  # Создайте пустой файл example.txt в текущей директории

try:
    # Инициализация драйвера (Chrome)
    driver = webdriver.Chrome()

    # Открытие страницы
    driver.get("http://suninjuly.github.io/file_input.html")

    # Заполнение текстовых полей
    driver.find_element(By.NAME, "firstname").send_keys("Иван")
    driver.find_element(By.NAME, "lastname").send_keys("Иванов")
    driver.find_element(By.NAME, "email").send_keys("ivan@example.com")

    # Загрузка файла
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажатие кнопки "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидание результата и получение числа из алерта
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Полученное число:", alert_text.split()[-1])
    alert.accept()

finally:
    # Закрытие браузера
    driver.quit()