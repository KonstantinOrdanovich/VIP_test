import TestHelper
import unittest
from selenium import webdriver
import random

emailId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)"
existerEmail = "ninja@test.com"
passwordId = "password"
registerId = "register"
singUpId = ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)"
testemail = "acyll" + str(random.randint(100, 9999)) + "@armyspy.com"
termsId = ".box"
error1 = "An Account Is Already Registered With Your Email Address. Please Login."
error2 = "You Must Agree To The Terms Before Registering!"
error3 = "Please Enter An Account Password."
server = "https://uat.vipoutlet.com"


class VipOutletTestRegister(unittest.TestCase):
    def test_valid_register(self):
        self.driver = webdriver.Firefox()
        self.driver.get(server)
        self.driver.find_element_by_css_selector(singUpId).click()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test()
        email = self.driver.find_element_by_css_selector(emailId)
        email.send_keys(existerEmail)
        password = self.driver.find_element_by_name(passwordId)
        password.clear()
        password.send_keys("test")
        register = self.driver.find_element_by_name(registerId)
        register.click()
        if error1 in self.driver.page_source:
            print "Case"+error1+"-pass"
        else:
            print "Case"+error1+" - false"
        self.driver.close()

    def test_valid_policies(self):
        self.driver = webdriver.Firefox()
        self.driver.get(server)
        self.driver.find_element_by_css_selector(singUpId).click()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test()
        email = self.driver.find_element_by_css_selector(emailId)
        email.clear()
        email.send_keys(testemail)
        password = self.driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test")
        register = self.driver.find_element_by_name("register")
        register.click()
        if error2 in self.driver.page_source:
            print "Case" +error2+"- Pass"
        else:
            print "Case " +error2+"- false"
        self.driver.close()

    def test_valid_password(self):
        self.driver = webdriver.Firefox()
        self.driver.get(server)
        self.driver.find_element_by_css_selector(singUpId).click()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test()
        email = self.driver.find_element_by_css_selector(emailId)
        email.clear()
        email.send_keys(testemail)
        terms = self.driver.find_element_by_css_selector(termsId)
        terms.click()
        register = self.driver.find_element_by_name(registerId)
        register.click()
        if error3 in self.driver.page_source:
            print "Case "+error3+"- Pass"
        else:
            print "Case"+error3+"- false"
        self.driver.close()
    def tearDown(self):
        self.driver.close()

