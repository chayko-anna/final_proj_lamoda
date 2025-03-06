from selene import browser, be


class CartPage:
    @staticmethod
    def open():
        browser.open('/checkout/cart/')

    @staticmethod
    def adding_item_to_cart():
        browser.element('[class="x-button x-button_primaryPremium x-button_48 _cartButton_1gbkc_11"]').should(be.visible).click()

    @staticmethod
    def check_if_item_added_to_cart():
        browser.open("/checkout/cart/")
        browser.element('[data-quick="MP002XW0FXPS"]').should(be.visible)

    @staticmethod
    def remove_item_from_cart():
        browser.open("/checkout/cart/")
        browser.element('[class="x-button x-button_borderlessPrimary x-button_24 _root_unp9l_15"]').should(be.visible).click()
        browser.element('[class="x-button x-button_primaryFilledWeb7184 x-button_32 x-button_intrinsic-width _actionButton_4stt4_7"]').should(be.visible).click()
        browser.driver.refresh()

    @staticmethod
    def check_if_item_removed_from_cart():
        browser.open("/checkout/cart/")
        browser.element('[data-quick="MP002XW0FXPS"]').should(be.absent)
