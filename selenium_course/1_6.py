from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Заполняем поле "First name"
    input1 = browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Иван")

    # Заполняем поле "Last name"
    last_name_input = browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name_input.send_keys("Петров")

    # Заполняем поле "Email"
    email_input =browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email_input.send_keys("ivan.petrov@example.com")

    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "input[class='form-control second']")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
  