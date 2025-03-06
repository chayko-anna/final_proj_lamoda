import allure

from models.ui.favorites import ClothesFavPage
from models.ui.pages import BasePage


@allure.tag('Browser')
@allure.epic('Favorites')
@allure.testcase('Successful adding to favorites')
def test_add_to_favorites(browser_settings):
    base = BasePage
    fav = ClothesFavPage

    with allure.step('Open item page'):
        base.open_item_page()

    with allure.step('Click add to fav button'):
        fav.adding_item_to_favorites()

    with allure.step('Go to fav page'):
        fav.open()

    with allure.step('Check that item is added'):
        fav.check_if_item_added_to_fav()


@allure.testcase('Successful removing from favorites')
def test_remove_from_favorites(browser_settings):
    base = BasePage
    fav = ClothesFavPage

    with allure.step('Open item page'):
        base.open_item_page()

    with allure.step('Click add to fav button'):
        fav.adding_item_to_favorites()

    with allure.step('Go to fav page'):
        fav.open()

    with allure.step('Click remove from fav button'):
        fav.removing_item_from_fav()

    with allure.step('Check that item is removed'):
        fav.check_if_item_removed_to_fav()
