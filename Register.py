import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from TestHelper import *
from creditCardGenerator import mastercard
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ErrorHandlingRegistration import *


class helpernavigate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_1_errorhandlingregistration(self):
        ErrorHandlingRegistration

    def test_1_register(self):
        driver = self.driver
        driver.get(server)
        signup = driver.find_element_by_css_selector(".header__profile-login-links > div:nth-child(3) > a:nth-child(1)")
        wait = WebDriverWait(driver, 4)
        element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.header__profile-login-links > div:nth-child(3) > a:nth-child(1)')))
        signup.click()
        username = driver.find_element_by_css_selector(
            "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(1)")
        username.click()
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
        if "An Account Is Already Registered With Your Email Address. Please Login." in driver.page_source:
            email = driver.find_element_by_css_selector(
                "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
            email.clear()
            email.send_keys(testemail2)
            password = driver.find_element_by_name("password")
            password.clear()
            password.send_keys("test")
            terms = driver.find_element_by_css_selector(".box")
            terms.click()
            register = driver.find_element_by_name("register")
            register.click()
            print "User " + testemail2 + " registered"
        else:
            print "User " + testemail + " registered"
        product = driver.find_element_by_css_selector(
            "div.carousel-row:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
        product.click()
        while False:
            try:
                assert "[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product" in driver.page_source
            except NoSuchElementException:
                print "Can't add product to cart for first time user -[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product "
                driver.close()
        addtocart = driver.find_element_by_css_selector(".single_add_to_cart_button")
        addtocart.click()
        addpayment = driver.find_element_by_css_selector(
            ".payment-row-box > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)")
        addpayment.click()
        mascard = driver.find_element_by_css_selector("#MC")
        mascard.click()
        credcard = driver.find_element_by_css_selector(
            "#wc-authorize-net-cim-credit-card-account-number").clear()
        driver.execute_script(
            "document.querySelector('#wc-authorize-net-cim-credit-card-account-number').value=" + str(
                mastercard) + "")

        cardholder = driver.find_element_by_css_selector("#wc-authorize-net-cim-credit-card-holder-name")
        cardholder.send_keys("K Tester")
        CVV = driver.find_element_by_css_selector("#wc-authorize-net-cim-credit-card-csc")
        CVV.send_keys("321")
        addaddressCheckout = driver.find_element_by_css_selector(".add-new-address-icon-wrapper")
        addaddressCheckout.click()
        firstNameCheckout = driver.find_element_by_css_selector("#billing_first_name")
        firstNameCheckout.send_keys("konstantin")
        lastnameCheckout = driver.find_element_by_css_selector("#billing_last_name")
        lastnameCheckout.send_keys("Tester")
        driver.execute_script("document.querySelector('#billing_phone').value =" + str(phone) + "")
        company = driver.find_element_by_css_selector("#billing_company")
        company.send_keys("TRG")
        address = driver.find_element_by_css_selector("#billing_address_1")
        address.send_keys("1835 E Hallandale Beach BLVD # 618")
        cityCheckout = driver.find_element_by_css_selector("#billing_city")
        cityCheckout.send_keys("Hallandale Beach")
        state = driver.find_element_by_css_selector(
            "#billing_state_field > span:nth-child(3) > span:nth-child(1) > span:nth-child(1)")
        state.click()
        state.send_keys("Florida")
        state.send_keys(Keys.ENTER)
        zipcode = driver.find_element_by_css_selector("#billing_postcode")
        zipcode.send_keys("33009")
        savepayment = driver.find_element_by_css_selector("div.small-12:nth-child(7) > button:nth-child(1)")
        savepayment.click()
