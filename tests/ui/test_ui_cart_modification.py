import allure

from models.ui.cart import CartPage
from models.ui.pages import BasePage


@allure.tag('Browser')
@allure.epic('Cart')
@allure.testcase('Successful adding to cart')
def test_add_to_cart_successful(browser_settings):
    cart = CartPage
    base = BasePage

    with allure.step('Open item page'):
        base.open_item_page('/p/mp002xw0fxps/clothes-markformelle-noski-pary/')

    with allure.step('Click add to cart button'):
        base.select_size()

    with allure.step('Click add to cart button'):
        cart.adding_item_to_cart()

    with allure.step('Go to cart page'):
        cart.open()

    with allure.step('Check that item is in cart'):
        cart.check_if_item_added_to_cart()


@allure.testcase('Out of stock')
def test_item_is_out_of_stock(browser_settings):
    base = BasePage

    with allure.step('Open item page'):
        base.open_item_page('/p/rtladn298701/clothes-wrangler-dzhinsy/')

    with allure.step('Check add to cart button'):
        base.check_availability()


@allure.testcase('Successful removing from cart')
def test_remove_from_cart(browser_settings):
    cart = CartPage
    base = BasePage

    with allure.step('Open item page'):
        base.open_item_page('/p/mp002xw0fxps/clothes-markformelle-noski-pary/')

    with allure.step('Click add to cart button'):
        base.select_size()

    with allure.step('Click add to cart button'):
        cart.adding_item_to_cart()

    with allure.step('Go to cart page'):
        cart.open()

    with allure.step('Check that item is in cart'):
        cart.check_if_item_added_to_cart()

    with allure.step('Remove item from cart'):
        cart.remove_item_from_cart()

    with allure.step('Check that item is not in cart'):
        cart.check_if_item_removed_from_cart()
