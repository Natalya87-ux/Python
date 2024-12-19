import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.InventoryPageInternetShop import InventoryPageInternetShop
from Pages.CartPageInternetShop import CartPageInternetShop
from Pages.CheckoutPageInternetShop import CheckoutPageInternetShop
from Pages.CheckoutOverviewPageInternetShop import OverviewPage
from Pages.MainPageInternetShop import MainPageInternetShop


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_Calc():
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
    shop = OverviewPage(driver)
    shop.set_cookie_policy()
    shop.wait()
    txt = shop.Equal()
    assert txt == 'Total: $58.29', 'Error!'
