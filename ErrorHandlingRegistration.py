import unittest
from os import wait
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from TestHelper import *


class ErrorHandlingRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        helper = Helper()
        helper.helrep()

    def test_1_exist_email(self):
        print testemail
        # wait = WebDriverWait(driver, 4)
        # element = wait.until(EC.visibility_of_element_located(
        #     (By.CSS_SELECTOR, 'div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)')))
        email = self.driver.find_element_by_css_selector(
            "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
        email.send_keys(existedEmail)
        password = self.driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test")
        register = self.driver.find_element_by_name("register")
        register.click()
        if " An Account Is Already Registered With Your Email Address. Please Login." in driver.page_source:
            print "An Account Is Already Registered With Your Email Address. Please Login. -pass"
        else:
            print "An Account Is Already Registered With Your Email Address. Please Login. - false"
        self.driver.close()

        # def test_2_policies(self):
        #     helper = Helper()
        #     helper.helrep()
        #     # driver = self.driver
        #     # driver.get(server)
        #     # signup = self.driver.find_element_by_css_selector(
        #     #     ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)")
        #     # signup.click()
        #     # username = driver.find_element_by_css_selector(
        #     #     "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(1)")
        #     # username.click()
        #     # username.clear()
        #     # username.send_keys("Konstantin")
        #     # lastname = driver.find_element_by_css_selector(
        #     #     "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(2)")
        #     # lastname.clear()
        #     # lastname.send_keys("Tester")
        #     print  testemail
        #     email = self.driver.find_element_by_css_selector(
        #         "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
        #     email.clear()
        #     email.send_keys(testemail)
        #     password = self.driver.find_element_by_name("password")
        #     password.clear()
        #     password.send_keys("test")
        #     register = self.driver.find_element_by_name("register")
        #     register.click()
        #     if "You Must Agree To The Terms Before Registering!" in driver.page_source:
        #         print "Terms and Policies - Pass"
        #     else:
        #         print "Terms and Policies - false"
        #     self.driver.close()
        #
        def test_3_password(self):
            driver = self.driver
            driver.get(server)
            signup = self.driver.find_element_by_css_selector(
                ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)")
            signup.click()
            username = driver.find_element_by_css_selector(
                "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(1)")
            username.click()
            username.clear()
            username.send_keys("Konstantin")
            lastname = driver.find_element_by_css_selector(
                "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(2)")
            lastname.clear()
            lastname.send_keys("Tester")
            print  testemail
            email = driver.find_element_by_css_selector(
                "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
            email.clear()
            email.send_keys(testemail)
            terms = driver.find_element_by_css_selector(".box")
            terms.click()
            register = driver.find_element_by_name("register")
            register.click()
            if "Please Enter An Account Password." in driver.page_source:
                print "Please Enter An Account Password. - Pass"
            else:
                print "Please Enter An Account Password. - false"
            driver.close()

        # def test_4_forgot_password(self):
        #     driver = self.driver
        #     driver.get(server)
        #     login = driver.find_element_by_css_selector(".header__profile-login-links > div:nth-child(1) > a:nth-child(1)")
        #     login.click()
        #     forgot = driver.find_element_by_css_selector("div.signup-link:nth-child(4) > a:nth-child(1)")
        #     forgot.click()
        #     email = driver.find_element_by_css_selector("#user_login")
        #     email.send_keys(testemail3)
        #     reset = driver.find_element_by_css_selector(".woocommerce-Button")
        #     reset.click()
        #     assert "A password reset email has been sent to the email address on file for your account, but may take several minutes to show up in your inbox. Please wait at least 10 minutes before attempting another reset." in driver.page_source
        #     assert "Password reset email has been sent." in driver.page_source
        #
        # def tearDown(self):
        #     self.driver.quit()
        #
