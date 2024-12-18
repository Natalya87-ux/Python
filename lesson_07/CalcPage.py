from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.MainPageСalculator import MainPageСalculator
from selenium.webdriver.chrome.options import Options



def testCalc():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options) 
    calc = MainPageСalculator(driver)
    calc.set_cookie_policy()
    calc.wait()
    calc.enter_time_delay(45)
    calc.enter_expression()
    calc.check_result()
    

    