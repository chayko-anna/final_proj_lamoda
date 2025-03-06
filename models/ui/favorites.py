from selene import browser, be


class ClothesFavPage:
    @staticmethod
    def open():
        browser.open('/wishlist/')

    @staticmethod
    def adding_item_to_fav():
        browser.element('[class="icon icon_heart-product icon_direction-down icon_44 undefined"]').should(
            be.visible).click()

    @staticmethod
    def check_if_item_added_to_fav():
        browser.open('/wishlist/')
        browser.element('[data-quick="MP002XW0FXPS"]').should(be.visible)

    @staticmethod
    def removing_item_from_fav():
        browser.open('/wishlist/')
        browser.element('[class="icon icon_heart-catalog-added icon_direction-down icon_24 undefined _iconAdded_1k70o_93"]').should(be.visible).click()
        browser.driver.refresh()

    @staticmethod
    def check_if_item_removed_to_fav():
        browser.open('/wishlist/')
        browser.element('[data-quick="MP002XW0FXPS"]').should(be.absent)
