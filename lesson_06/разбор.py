#№1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера (убедитесь, что Chromedriver установлен)
driver = webdriver.Chrome()

try:
    # Переходим на нужную страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Находим синюю кнопку и нажимаем на нее
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    
    # Ждем, пока текст появится в зеленой плашке
    alert_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ajax-content"))
    )
    
    # Получаем текст из зеленой плашки
    alert_text = alert_div.text
    
    # Выводим текст в консоль
    print(alert_text)  # Ожидается: "Data loaded with AJAX get request."
    
finally:
    # Закрываем драйвер
    driver.quit()
    
	
#N2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера (убедитесь, что Chromedriver установлен и доступен в PATH)
driver = webdriver.Chrome()

try:
    # Переходим на нужную страницу
    driver.get("http://uitestingplayground.com/textinput")
    
    # Находим поле ввода и указываем текст
    input_field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
    input_field.send_keys("SkyPro")
    
    # Находим синюю кнопку и нажимаем на нее
    button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
    button.click()
    
    # Получаем текст кнопки после нажатия
    button_text = button.text
    
    # Выводим текст в консоль
    print(button_text)  # Ожидается: "SkyPro"
    
finally:
    # Закрываем драйвер
    driver.quit()
    
#N3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера (убедитесь, что Chromedriver установлен и доступен в PATH)
driver = webdriver.Chrome()

try:
    # Переходим на нужную страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ожидаем, пока все изображения загрузятся
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
    )
    
    # Находим все изображения
    images = driver.find_elements(By.TAG_NAME, 'img')
    
    # Получаем значение атрибута src у 3-й картинки (индекс 2)
    src_value = images[2].get_attribute('src')
    
    # Выводим значение в консоль
    print(src_value)

finally:
    # Закрываем драйвер
    driver.quit()