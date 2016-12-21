import random
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

testemail = ("acyll" + str(random.randint(2000, 7000)) + "@armyspy.com")
testemail2 = ("acyll" + str(random.randint(7000, 9000)) + "@armyspy.com")
testemail3 = "acyll1988@armyspy.com"
server = "https://uat.vipoutlet.com"
phone = random.randint(100000000000, 999999999999)
existedEmail = "ninja@test.com"


class LoginPage():
    username = "Konstantin"
    lastname = "Tester"
    signupFieldId = ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)"
    usernameFileldId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(1)"
    lastmameFieldId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(2)"
    server = "https://uat.vipoutlet.com"
    existedEmail = "https://uat.vipoutlet.com"

    def __init__(self, driver):
        self.driver = driver
        self.usernameElement = self.driver.find_element_by_css_selector(self.usernameFileldId)
        self.lastnameElement = self.driver.find_element_by_css_selector(self.lastmameFieldId)

    def signUp_test(self):
        self.usernameElement.send_keys(self.username)
        self.lastnameElement.send_keys(self.lastname)

class CheckoutPage():

    def __init__(self,driver):
        self.driver = driver



