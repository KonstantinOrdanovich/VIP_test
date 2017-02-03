import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import TestHelper
import Checkout

class navigateToCheckout(unittest.TestCase):
    def test_2(self):
        # self.driver = webdriver.PhantomJS(executable_path='/Users/user/phantomjs-2.1.1-macosx/bin/phantomjs')
        self.driver =webdriver.Firefox()
        self.driver.get(TestHelper.server)
        navigate = Checkout.VipOutletTestCheckout(self.driver)
        navigate.testCheckout()
        placeOrder = TestHelper.AddAddressCheckout(self.driver)
        while True:
            try:
                placeOrder.placeOrder()
            except WebDriverException:
                print "Unable to click Place Order, retrying"
            else:
                break
        while True:
            try:
                orderID = self.driver.find_element_by_css_selector(".order-id-row__id > a:nth-child(1)")
            except NoSuchElementException:
                print "Waiting Page reload"
            else:
                break
        while True:
            try:
                orderIdElement = self.driver.find_element_by_css_selector(TestHelper.orderId)
                print "Order Number "+orderIdElement.text+" is created"
                orderIdElement.click()
            except WebDriverException:
                print "Unable to click Order ID, retrying"
            else:
                break

