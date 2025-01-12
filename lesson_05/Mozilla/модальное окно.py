
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

try:
    driver.get('http://the-internet.herokuapp.com/entry_ad')
    button = driver.find_element
    (By.CLASS_NAME, "modal-footer")
    sleep(10)
    button.click()
except NoSuchElementException:
    driver.quit()
sys.exit(1)
