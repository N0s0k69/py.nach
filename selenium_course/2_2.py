from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Функция для вычисления суммы чисел на странице
def calculate_sum(driver):
    num1 = int(driver.find_element(By.ID, "num1").text)
    num2 = int(driver.find_element(By.ID, "num2").text)
    return str(num1 + num2)

# Основной код
try:
    # Инициализация драйвера (в данном случае используется Chrome)
    driver = webdriver.Chrome()

    # Открытие страницы
    driver.get("https://suninjuly.github.io/selects1.html")

    # Вычисление суммы
    total_sum = calculate_sum(driver)

    # Выбор значения в выпадающем списке
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total_sum)

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