import unittest
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from TestHelper import *


class helpernavigate(unittest.TestCase):
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




