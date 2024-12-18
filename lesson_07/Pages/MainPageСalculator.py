from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageСalculator:
    def __init__(self,driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
        

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self._driver.add_cookie(cookie)
        

    def wait(self):
        WebDriverWait(self._driver, 25).until(
        EC.presence_of_all_elements_located((By.ID, "delay"))
        )
        

    def enter_time_delay(self, delay):
        self._driver.find_element(By.ID,'delay').clear()
        input_field = self._driver.find_element(By.ID,'delay')
        input_field.send_keys(delay)
        

    def enter_expression(self):
        keynums = self._driver.find_element(By.XPATH,"//span[contains(.,'7')]")
        keynums.click()
        keynums = self._driver.find_element(By.XPATH,"//span[contains(.,'+')]")
        keynums.click()
        keynums = self._driver.find_element(By.XPATH,"//span[contains(.,'8')]")
        keynums.click()
        keynums = self._driver.find_element(By.XPATH,"//span[contains(.,'=')]")
        keynums.click()
        
    
    def check_result(self):
        WebDriverWait(self._driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"),'15'))
        t = self._driver.find_element(By.CLASS_NAME,'screen')
        assert t.text == '15', 'ОШИБКА?!'
        
