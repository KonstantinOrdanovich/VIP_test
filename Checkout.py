import unittest
from selenium import webdriver
from Register import *
from RegisterTestFull import *

class testCheckout(unittest.TestCase):
    def test_1_Login(self):
        helpernavigate.test_1_register


    def tearDown(self):
        self.driver.quit()










