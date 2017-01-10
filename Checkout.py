import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from creditCardGenerator import mastercard
import TestHelper
import random


class values():

    productId = "div.carousel-row:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
    error1 = "An Account Is Already Registered With Your Email Address. Please Login."
    error2 = "You Must Agree To The Terms Before Registering!"
    error3 = "Please Enter An Account Password."

class VipOutletTestCheckout(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
    def test_1_register(self):
        HomePage = TestHelper.HomePage(self.driver)
        HomePage.signUpClick()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test_full()
        sign_up.registerClick()
        if values.error1 in self.driver.page_source:
            sign_up.signUp_else()
            sign_up.registerClick()
            print "User " + TestHelper.testemail2 + " registered"
        else:
            print "User " + TestHelper.testemail + " registered"
        HomePage.productOnHomePage()
        while False:
            try:
                assert "[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product" in self.driver.page_source
            except NoSuchElementException:
                print "Can't add product to cart for first time user -[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product "
                self.driver.close()
            else:
                print "Autotest over"
                break
        addtocart = TestHelper.addtoCartProductPage(self.driver)
        addtocart.addToCart()
        checkout = TestHelper.AddAddressCheckout(self.driver)
        while True:
            try:
                checkout.addPaymentCheckout()
            except WebDriverException,e:
                print "Unable to click Add Payment in Checkout, retrying"
            else:
                break
        checkout.credit_card_checkout()
        checkout.addAddressIcon()
        checkout.add_address_checkout()
        checkout.addAddressCheckoutPayment()


