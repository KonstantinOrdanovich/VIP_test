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
        mascard = self.driver.find_element_by_css_selector("#MC")
        mascard.click()
        credcard = self.driver.find_element_by_css_selector(
            "#wc-authorize-net-cim-credit-card-account-number").clear()
        self.driver.execute_script(
            "document.querySelector('#wc-authorize-net-cim-credit-card-account-number').value=" + str(
                mastercard) + "")

        cardholder = self.driver.find_element_by_css_selector("#wc-authorize-net-cim-credit-card-holder-name")
        cardholder.send_keys("K Tester")
        CVV = self.driver.find_element_by_css_selector("#wc-authorize-net-cim-credit-card-csc")
        CVV.send_keys("321")
        addaddressCheckout = self.driver.find_element_by_css_selector(".add-new-address-icon-wrapper")
        addaddressCheckout.click()
        firstNameCheckout = self.driver.find_element_by_css_selector("#billing_first_name")
        firstNameCheckout.send_keys("konstantin")
        lastnameCheckout = self.driver.find_element_by_css_selector("#billing_last_name")
        lastnameCheckout.send_keys("Tester")
        self.driver.execute_script("document.querySelector('#billing_phone').value =" + str(values.phone) + "")
        company = self.driver.find_element_by_css_selector("#billing_company")
        company.send_keys("TRG")
        address = self.driver.find_element_by_css_selector("#billing_address_1")
        address.send_keys("1835 E Hallandale Beach BLVD # 618")
        cityCheckout = self.driver.find_element_by_css_selector("#billing_city")
        cityCheckout.send_keys("Hallandale Beach")
        state = self.driver.find_element_by_css_selector(
            "#billing_state_field > span:nth-child(3) > span:nth-child(1) > span:nth-child(1)")
        state.click()
        state.send_keys("Florida")
        state.send_keys(Keys.ENTER)
        zipcode = self.driver.find_element_by_css_selector("#billing_postcode")
        zipcode.send_keys("33009")
        savepayment = self.driver.find_element_by_css_selector("div.small-12:nth-child(7) > button:nth-child(1)")
        savepayment.click()
        while True:
            try:
                placeOrder = self.driver.find_element_by_css_selector(values.placeOrderId)
                placeOrder.click()
            except WebDriverException, e:
                print "Unable to click Place Order, retrying"
            else:
                break
        
        orderIdElement = self.driver.find_element_by_css_selector(values.orderId)
        print "Order " + orderIdElement + "has been created"
        orderIdElement.click()
