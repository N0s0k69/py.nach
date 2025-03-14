from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения математической функции
def calculate_function(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Инициализация драйвера (Chrome)
    driver = webdriver.Chrome()

    # Открытие страницы
    driver.get("http://suninjuly.github.io/alert_accept.html")

    # Нажатие на кнопку для вызова confirm
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Принятие confirm
    confirm = driver.switch_to.alert
    confirm.accept()

    # Решение капчи
    # Считывание значения переменной x
    x_value = driver.find_element(By.ID, "input_value").text

    # Вычисление математической функции
    result = calculate_function(x_value)

    # Ввод результата в текстовое поле
    text_field = driver.find_element(By.ID, "answer")
    text_field.send_keys(result)

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