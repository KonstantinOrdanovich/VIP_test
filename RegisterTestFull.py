import unittest
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from TestHelper import *


class helpernavigatefull(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_1_register(self):
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
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test")
        terms = driver.find_element_by_css_selector(".box")
        terms.click()
        register = driver.find_element_by_name("register")
        register.click()


    def test_2_login(self, testemail):
        driver = self.driver
        driver.get(server)
        login = driver.find_element_by_css_selector(".header__profile-login-links > div:nth-child(1) > a:nth-child(1)")
        login.click()
        username = driver.find_element_by_name("username")
        username.send_keys(testemail)
        password = driver.find_element_by_name("password")
        password.send_keys("test")
        loginbutton = driver.find_element_by_name("login")
        loginbutton.click()



    def test_3_logout(self):
        driver = self.driver
        driver.get(server)
        login = driver.find_element_by_css_selector(".header__profile-login-links > div:nth-child(1) > a:nth-child(1)")
        login.click()
        username = driver.find_element_by_name("username")
        username.send_keys("ninja")
        password = driver.find_element_by_name("password")
        password.send_keys("test")
        loginbutton = driver.find_element_by_name("login")
        loginbutton.click()
        logout = driver.find_element_by_css_selector(".header__profile-logout")
        logout.click()


    def test_4_forgot_password(self):
        driver = self.driver
        driver.get(server)
        login = driver.find_element_by_css_selector(".header__profile-login-links > div:nth-child(1) > a:nth-child(1)")
        login.click()
        forgot = driver.find_element_by_css_selector("div.signup-link:nth-child(4) > a:nth-child(1)")
        forgot.click()
        email = driver.find_element_by_css_selector("#user_login")
        email.send_keys(testemail3)
        reset = driver.find_element_by_css_selector(".woocommerce-Button")
        reset.click()
        assert "A password reset email has been sent to the email address on file for your account, but may take several minutes to show up in your inbox. Please wait at least 10 minutes before attempting another reset." in driver.page_source
        assert "Password reset email has been sent." in driver.page_source

    def tearDown(self):
        self.driver.quit()

