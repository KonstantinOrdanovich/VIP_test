import unittest
from selenium import webdriver
import random

testemail = ("test"+str(random.randint(2000,7000))+"@test.com")

class helpernavigate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_1_register(self):
        driver= self.driver
        driver.get("https://uat.vipoutlet.com")
        signup = self.driver.find_element_by_css_selector(
            ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)").click()
        username = driver.find_element_by_css_selector("div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(1)")
        username.click()
        username.clear()
        username.send_keys("Konstantin")
        lastname = driver.find_element_by_css_selector("div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(2)")
        lastname.clear()
        lastname.send_keys("Tester")
        email = driver.find_element_by_css_selector("div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
        email.clear()
        email.send_keys(testemail)
        password= driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test")
        terms = driver.find_element_by_css_selector(".box")
        terms.click()
        register = driver.find_element_by_name("register")
        register.click()

    def test_2_logout(self):
        driver = self.driver
        self.driver.get("https://uat.vipoutlet.com")
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




def test_end(self):
    self.driver.close()









