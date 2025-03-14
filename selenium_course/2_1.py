from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения выражения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Инициализация веб-драйвера (например, Chrome)
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://suninjuly.github.io/get_attribute.html")

    # Поиск элемента-картинки (сундука)
    chest = driver.find_element(By.ID, "treasure")

    # Получение значения атрибута valuex
    x_value = chest.get_attribute("valuex")

    # Вычисление значения функции
    result = calc(x_value)

    # Ввод результата в текстовое поле
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отметка checkbox "I'm the robot"
    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбор radiobutton "Robots rule!"
    robots_rule_radio = driver.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажатие на кнопку "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидание для визуальной проверки результата
    time.sleep(10)

finally:
    # Закрытие браузера
    driver.quit()