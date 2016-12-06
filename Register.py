import unittest
from selenium import webdriver

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_Register(self):
        driver=self.driver
        driver.get("https://uat.vipoutlet.com")


