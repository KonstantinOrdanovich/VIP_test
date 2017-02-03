import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException,ElementNotVisibleException
import TestHelper
import Checkout

class editAddressinCheckout(unittest.TestCase):
    def test_2(self):
        self.driver = webdriver.Firefox()
        self.driver.get(TestHelper.server)
        navigate = Checkout.VipOutletTestCheckout(self.driver)
        if navigate.test_1_register():
            changePaymentClick = TestHelper.changePayment(self.driver)
            if changePaymentClick.chagePaymentClickCheckout():
                print "change Payment is clicked"
            else:
                changePaymentClick.chagePaymentClickCheckout()

        while True:
            try:
                addNewPaymentCheckout = TestHelper.addNewPaymentChekoutExisterPayment(self.driver)
                addNewPaymentCheckout.addNewPaymentCheckout()
            except NoSuchElementException, e:
                print "Button Add New Payment is missed"
            else:
                break

        addcreditcard =TestHelper.AddAddressCheckout(self.driver)
        if addcreditcard.credit_card_checkout():
            while True:
                try:
                    chooseAddress = TestHelper.chooseAddress(self.driver)
                    chooseAddress.chooseAddressAddPayment()
                except NoSuchElementException,e:
                    print "No exister address books in dropdown"
                else:
                    addcreditcard.addAddressCheckoutPayment()

