from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.MainPageForm import MainPageForm
from selenium.webdriver.chrome.options import Options



def testCalc():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options) 
    autoform = MainPageForm(driver)
    autoform.set_cookie_policy()
    autoform.waitbyname()
    autoform.fill_form_element()
    autoform.waitbyid()
    autoform.assert_red()
    autoform.assert_green()