import unittest
from selenium import webdriver
from creditCardGenerator import mastercard
import TestHelper
import random
class wm():
    wmserver = "https://www.directliquidation.com/vipoutlet-affiliate/"

class WalmartCheckout(unittest.TestCase):
    def test_walmart_checkout_1(self):
        self.driver = webdriver.Firefox()
        self.driver.get(wm.wmserver)
        wmcheckout = TestHelper.WalmartPage(self.driver)
        wmcheckout.walmart_checkout()
        wmlogin = TestHelper.LoginPage(self.driver)
        wmlogin.signUp_test_full()
        register = self.driver.find_element_by_name(TestHelper.registerId)
        register.click()
        if TestHelper.error1 in self.driver.page_source:
            wmlogin.signUp_else()
            register = self.driver.find_element_by_name(TestHelper.registerId)
            register.click()
            print "User " + TestHelper.testemail2 + " registered"
        else:
            print "User " + TestHelper.testemail + " registered"

