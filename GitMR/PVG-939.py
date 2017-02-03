import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException,ElementNotVisibleException
import TestHelper
import Checkout

class PVG939(unittest.TestCase):
    def test_PVG939(self):
        self.driver = webdriver.Firefox()
        self.driver.get(TestHelper.server)
        navigate = Checkout.VipOutletTestCheckout(self.driver)
        navigate.test_1_register()
        addNewCreditCard = TestHelper.AddAddressCheckout(self.driver)
        addNewCreditCard.cancelWishlistButton
