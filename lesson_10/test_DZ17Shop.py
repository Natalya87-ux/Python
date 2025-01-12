import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.InventoryPageInternetShop import InventoryPageInternetShop
from Pages.CartPageInternetShop import CartPageInternetShop
from Pages.CheckoutPageInternetShop import CheckoutPageInternetShop
from Pages.CheckoutOverviewPageInternetShop import OverviewPage
from Pages.MainPageInternetShop import MainPageInternetShop
import allure


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Internet Shop")
@allure.title("Test checkout process")
@allure.description("Testing the full checkout process in the internet shop")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_process(driver):
    with allure.step("Open main page and set cookie policy"):
        shop = MainPageInternetShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Login to the shop"):
        shop.enterloginpass()

    with allure.step("Navigate to inventory page and set cookie policy"):
        shop = InventoryPageInternetShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Add item to basket"):
        shop.additemintobasket()

    with allure.step("Navigate to cart page and set cookie policy"):
        shop = CartPageInternetShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Press checkout button"):
        shop.checkoutpress()

    with allure.step("Navigate to checkout page and set cookie policy"):
        shop = CheckoutPageInternetShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Press continue button"):
        shop.Continuepress()

    with allure.step("Navigate to overview page and set cookie policy"):
        shop = OverviewPage(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Verify total amount"):
        txt = shop.Equal()
        assert (
            txt == "Total: $58.29"
        ), f"Error! Expected 'Total: $58.29', but got '{txt}'"
