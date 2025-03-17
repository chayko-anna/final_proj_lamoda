import allure
from models.api.cart import Cart


@allure.epic('Cart')
@allure.testcase('Add to cart')
def test_successful_add_to_cart():
    cart = Cart()

    with allure.step("Successful add to cart"):
        cart.add_to_cart_successful()


@allure.testcase('Remove from cart')
def test_successful_remove_from_cart():
    cart = Cart()

    with allure.step("Successful add to cart"):
        cart.add_to_cart_successful()

    with allure.step("Successful remove from cart"):
        cart.remove_from_cart()


@allure.testcase('Unsuccessful add to cart')
def test_unsuccessful_add_to_cart():
    cart = Cart()

    with allure.step("No item in stock: add to cart"):
        cart.add_to_cart_failed()
