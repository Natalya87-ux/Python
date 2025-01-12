from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys

# Установка Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

# Открыть страницу
try:
    driver.get('http://the-internet.herokuapp.com/inputs')
    input_selector = "div #content"
    driver.find_element(By.CSS_SELECTOR, input_selector)
    print("Сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# Введите в поле текст 1000
input = driver.find_element(By.CSS_SELECTOR, "input")
input.send_keys("1000")
print("написала 1000")
sleep(1)

# Очистите это поле
input.clear()
print("очистила")
sleep(1)


input.send_keys("999")
print("написала 999")
sleep(5)

# Прерывание работы драйвера
driver.quit()
