from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys

# Установка Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(
                                                                            )))

# Открыть страницу
try:
    driver.get('http://the-internet.herokuapp.com/login')
    print("Сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

modul_selector = "username"
input = driver.find_element(By.ID, modul_selector)
input.send_keys("tomsmith")


modul_selector = "password"
input = driver.find_element(By.ID, modul_selector)
input.send_keys("SuperSecretPassword!")

modul_selector = "radius"
button = driver.find_element(By.CLASS_NAME, modul_selector)
sleep(3)
button.click()
print("Mamavdele!")