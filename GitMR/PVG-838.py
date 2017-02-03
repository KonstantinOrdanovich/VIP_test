import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from creditCardGenerator import mastercard
import TestHelper



class PVG838(unittest.TestCase):
    def test_1_register(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(TestHelper.server2)
        HomePage = TestHelper.HomePage(self.driver)
        HomePage.search()
        while True:
            try:
                signUpSearch = TestHelper.SearchPage(self.driver)
                signUpSearch.signUpSearch()
            except WebDriverException:
                print "Register button is not loaded, wait"
            else:
                break
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test_full()
        sign_up.registerClick()
        if TestHelper.error1 in self.driver.page_source:
            sign_up.signUp_else()
            sign_up.registerClick()
            print "User " + TestHelper.testemail2 + " registered"
        else:
            print "User " + TestHelper.testemail + " registered"
        print self.driver.current_url
        url = self.driver.current_url
        if url == "https://pvg-838-invalid-redirect-on-sign-in.dev.vipoutlet.com/shop/?s=":
            print "PVG 838 is Done"
        else:
            print "PVG 838 is Failed"

    def tearDown(self):
        self.driver.close()


