import unittest
from selenium import webdriver
import TestHelper


class VipOutletGuestCheckout(unittest.TestCase):
    def test_guestCheckout(self):
        self.driver = webdriver.Firefox()
        self.driver.get(TestHelper.server)
        product = TestHelper.HomePage(self.driver)
        product.productOnHomePage()
        addToCart =TestHelper.addtoCartProductPage(self.driver)
        addToCart.addToCart()
        addressGuestCheckout = TestHelper.AddAddressCheckout(self.driver)
        addressGuestCheckout.add_address_checkout()


