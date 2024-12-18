from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.InventoryPageInternetShop import InventoryPageInternetShop
from Pages.CartPageInternetShop import CartPageInternetShop
from Pages.CheckoutPageInternetShop import CheckoutPageInternetShop
from Pages.CheckoutOverviewPageInternetShop import CheckoutOverviewPageInternetShop
from Pages.MainPageInternetShop import MainPageInternetShop

def testCalc():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options) 
    shop = MainPageInternetShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.enterloginpass()
    shop = InventoryPageInternetShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.additemintobasket()
    shop = CartPageInternetShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.checkoutpress()
    shop = CheckoutPageInternetShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.Continuepress()
    shop = CheckoutOverviewPageInternetShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.Equal()

    