import unittest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import TestHelper

class Registration(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
    def test_register(self):
        HomePage = TestHelper.HomePage(self.driver)
        HomePage.signUpClick()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test_full()
        while True:
            try:
                sign_up.registerClick()
            except WebDriverException:
                print "Button is not available"
            else:
                break
        if TestHelper.error1 in self.driver.page_source:
            sign_up.signUp_else()
            sign_up.registerClick()
            print "User " + TestHelper.testemail2 + " registered"
        else:
            print "User " + TestHelper.testemail + " registered"
        print self.driver.current_url
        url = self.driver.current_url
        if url == "https://uat.vipoutlet.com/":
            print "PVG 838 is Done - After Login on version page redirect to My Account, should on Home Page"
        else:
            print "PVG 838 is Failed"