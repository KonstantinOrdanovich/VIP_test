import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from creditCardGenerator import mastercard
import TestHelper
import random


class values():
    emailId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)"
    existerEmail = "ninja@test.com"
    passwordId = "password"
    registerId = "register"
    singUpId = ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)"
    productId = "div.carousel-row:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
    testemail = "acyll" + str(random.randint(100, 9999)) + "@armyspy.com"
    testemail1 = ("acyll" + str(random.randint(2000, 7000)) + "@armyspy.com")
    testemail2 = ("acyll" + str(random.randint(7000, 9000)) + "@armyspy.com")
    termsId = ".box"
    error1 = "An Account Is Already Registered With Your Email Address. Please Login."
    error2 = "You Must Agree To The Terms Before Registering!"
    error3 = "Please Enter An Account Password."
    server = "https://uat.vipoutlet.com/"
    phone = random.randint(100000000000, 999999999999)
    placeOrderId = "#place_order"
    orderId = ".order-id-row__id > a:nth-child(1)"
    addPaymentId = ".payment-row-box > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)"
    addAddressID = "div.small-12:nth-child(7) > button:nth-child(1)"

class VipOutletTestCheckout(unittest.TestCase):
    def test_1_register(self):
        self.driver = webdriver.Firefox()
        self.driver.get(values.server)
        self.driver.find_element_by_css_selector(values.singUpId).click()
        sign_up = TestHelper.LoginPage(self.driver)
        sign_up.signUp_test_full()
        register = self.driver.find_element_by_name(values.registerId)
        register.click()
        if values.error1 in self.driver.page_source:
            sign_up.signUp_else()
            register = self.driver.find_element_by_name(values.registerId)
            register.click()
            print "User " + values.testemail2 + " registered"
        else:
            print "User " + values.testemail + " registered"
        product = self.driver.find_element_by_css_selector(values.productId)
        product.click()
        while False:
            try:
                assert "[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product" in self.driver.page_source
            except NoSuchElementException:
                print "Can't add product to cart for first time user -[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product "
                self.driver.close()
            else:
                print "Autotest over"
                break
        addtocart = self.driver.find_element_by_css_selector(".single_add_to_cart_button")
        addtocart.click()
        while True:
            try:
                addpayment = self.driver.find_element_by_css_selector(values.addPaymentId)
                addpayment.click()
            except WebDriverException,e:
                print "Unable to click Add Payment in Checkout, retrying"
            else:
                break
        sign_up = TestHelper.CheckoutPage(self.driver)
        sign_up.credit_card_checkout()
        sign_up = TestHelper.AddAddressCheckout(self.driver)
        sign_up.add_address_checkout()
        savepayment = self.driver.find_element_by_css_selector(values.addAddressID)
        savepayment.click()
        while True:
            try:
                placeOrder = self.driver.find_element_by_css_selector(values.placeOrderId)
                placeOrder.click()
            except WebDriverException, e:
                print "Unable to click Place Order, retrying"
            else:
                break
        while True:
            try:
                orderIdElement = self.driver.find_element_by_css_selector(values.orderId)
                orderIdElement.click()
            except WebDriverException,e:
                print "Unable to click Order ID, retrying"
            else:
                break
    def tearDown(self):
        self.driver.close()
