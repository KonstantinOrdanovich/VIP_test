import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from creditCardGenerator import mastercard

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
    emailFieldId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)"
    passwordId = "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(4)"
    password = "test"
    termsId = ".box"
    registerId = ".standard-btn"


    def __init__(self, driver):
        self.driver = driver
        self.usernameElement = self.driver.find_element_by_css_selector(self.usernameFileldId)
        self.lastnameElement = self.driver.find_element_by_css_selector(self.lastmameFieldId)
        self.email = self.driver.find_element_by_css_selector(self.emailFieldId)
        self.passwordElement = self.driver.find_element_by_css_selector(self.passwordId)
        self.terms = self.driver.find_element_by_css_selector(self.termsId)

    def signUp_test(self):
        self.usernameElement.send_keys(self.username)
        self.lastnameElement.send_keys(self.lastname)

    def signUp_test_full(self):
        self.usernameElement.send_keys(self.username)
        self.lastnameElement.send_keys(self.lastname)
        self.email.send_keys(testemail)
        self.passwordElement.send_keys(self.password)
        self.terms.click()

    def signUp_else(self):
        self.usernameElement.send_keys(self.username)
        self.lastnameElement.send_keys(self.lastname)
        self.email.send_keys(testemail2)
        self.passwordElement.send_keys(self.password)
        self.terms.click()

class CheckoutPage():
    mascardId = "#MC"
    credcardId = "#wc-authorize-net-cim-credit-card-account-number"
    cardholderId = "#wc-authorize-net-cim-credit-card-holder-name"
    CVVId = "#wc-authorize-net-cim-credit-card-csc"


    def __init__(self,driver):
        self.driver = driver
        self.mascard = self.driver.find_element_by_css_selector(self.mascardId)
        self.credcard = self.driver.find_element_by_css_selector(self.credcardId)
        self.cardholder = self.driver.find_element_by_css_selector(self.cardholderId)
        self.CVVElement = self.driver.find_element_by_css_selector(self.CVVId)

    def credit_card_checkout(self):
        self.mascard.click()
        self.credcard.clear
        self.driver.execute_script("document.querySelector('#wc-authorize-net-cim-credit-card-account-number').value=" + str(
                mastercard) + "")
        self.cardholder.send_keys("K Tester")
        self.CVVElement.send_keys(str(random.randint(111,999)))

class AddAddressCheckout():
    addressId = ".add-new-address-icon-wrapper"
    firstNameId = "#billing_first_name"
    lastNameId = "#billing_last_name"
    companyId = "#billing_company"
    billingaddressId = "#billing_address_1"
    cityId = "#billing_city"
    stateId = "#billing_state_field > span:nth-child(3) > span:nth-child(1) > span:nth-child(1)"
    zipcodeId = "#billing_postcode"


    def __init__(self,driver):
        self.driver =driver
        self.addaddressCheckout = self.driver.find_element_by_css_selector(self.addressId)
        self.firstNameCheckout =self.driver.find_element_by_css_selector(self.firstNameId)
        self.lastnameCheckout = self.driver.find_element_by_css_selector(self.lastNameId)
        self.companyElement = self.driver.find_element_by_css_selector(self.companyId)
        self.addressElement = self.driver.find_element_by_css_selector(self.billingaddressId)
        self.cityElement = self.driver.find_element_by_css_selector(self.cityId)
        self.stateElement =self.driver.find_element_by_css_selector(self.stateId)
        self.zipcodeElement = self.driver.find_element_by_css_selector(self.zipcodeId)

    def add_address_checkout(self):
        self.addaddressCheckout.click()
        self.firstNameCheckout.send_keys("Konstantin")
        self.lastnameCheckout.send_keys("Tester")
        self.driver.execute_script("document.querySelector('#billing_phone').value =" + str(phone) + "")
        self.companyElement.send_keys("TRG")
        self.addressElement.send_keys("1835 E Hallandale Beach BLVD # 618")
        self.cityElement.send_keys("Hallandale Beach")
        self.stateElement.click()
        self.stateElement.send_keys("Florida")
        self.stateElement.send_keys(Keys.ENTER)
        self.zipcodeElement.send_keys("33009")




