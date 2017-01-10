import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import TestHelper
import Checkout

class navigateToCheckout(unittest.TestCase):
    def test_2(self):
        self.driver = webdriver.Firefox()
        self.driver.get(TestHelper.server)
        navigate = Checkout.VipOutletTestCheckout(self.driver)
        navigate.test_1_register()
        addNewCreditCard = TestHelper.AddAddressCheckout(self.driver)
        while True:
            try:
                placeOrder = TestHelper.AddAddressCheckout(self.driver)
                placeOrder.placeOrder()
            except WebDriverException:
                print "Unable to click Place Order, retrying"
            else:
                break
        while True:
            try:
                orderIdElement = self.driver.find_element_by_css_selector(TestHelper.orderId)
                orderIdElement.click()
            except WebDriverException:
                print "Unable to click Order ID, retrying"
            else:
                break
