import random
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from creditCardGenerator import mastercard

testemail = ("acyll" + str(random.randint(2000, 7000)) + "@armyspy.com")
testemail2 = ("acyll" + str(random.randint(7000, 9000)) + "@armyspy.com")
testemail3 = "acyll1988@armyspy.com"
server = "https://uat.vipoutlet.com"
server2 = "https://pvg-838-invalid-redirect-on-sign-in.dev.vipoutlet.com"
phone = random.randint(100000000000, 999999999999)
existedEmail = "ninja@test.com"
error1 = "An Account Is Already Registered With Your Email Address. Please Login."
error2 = "You Must Agree To The Terms Before Registering!"
error3 = "Please Enter An Account Password."
orderId = ".order-id-row__id > a:nth-child(1)"


class HomePage:
    signUpId = ".header__profile-login-links > div:nth-child(3) > a:nth-child(1)"
    # productId = "column small-12 text-center product-item__image"
    searchId = ".header-search__button"

    def __init__(self, driver):
        self.driver = driver
        self.signUpElement = self.driver.find_element_by_css_selector(self.signUpId)
        self.searchElement =self.driver.find_element_by_css_selector(self.searchId)

    # Click Sign Up button on Home Page
    def signUpClick(self):
        self.signUpElement.click()
    def search(self):
        self.searchElement.click()
    # def productOnHomePage(self):
    #     self.productElement = self.driver.execute_script(
    #         "jQuery(document.getElementsByClassName('" + self.productId + "')).eq(1).click()")

class addproductOnHomePage:
    productId = "column small-12 text-center product-item__image"
    def __init__(self,driver):
        self.driver = driver
    def productOnHomePage(self):
        self.productElement = self.driver.execute_script(
            "jQuery(document.getElementsByClassName('" + self.productId + "')).eq(1).click()")

class LoginPage:
    username = "Konstantin"
    lastname = "Tester"
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
        self.registerElement = self.driver.find_element_by_css_selector(self.registerId)

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
        self.email.clear()
        self.email.send_keys(testemail2)
        self.passwordElement.send_keys(self.password)
        self.terms.click()

    def registerClick(self):
        self.registerElement.click()

class CheckoutPage:
    addNewPaymentButtonId = ".payment-row-box > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)"
    placeOrderId = "#place_order"
    addtoWishlistCheckoutId = ".checkout__summary-item-links > span:nth-child(2) > a:nth-child(2)"
    checkwishlistCheckoutId = "div.link-column:nth-child(2) > a:nth-child(1) > strong:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver
        self.addNewPaymentButton = self.driver.find_element_by_css_selector(self.addNewPaymentButtonId)
        self.placeOrderElement = self.driver.find_element_by_css_selector(self.placeOrderId)
        self.addtoWishlistCheckoutElement = self.driver.find_element_by_css_selector(self.addtoWishlistCheckoutId)
        # self.checkwishlistCheckoutElement =self.driver.find_element_by_css_selector(self.checkwishlistCheckoutId)
    def addNewPaymentCheckout(self):
        self.addNewPaymentButton.click()

    def placeOrder(self):
        self.placeOrderElement.click()
    def addtoWishlistCheckoutMethod(self):
        self.addtoWishlistCheckoutElement.click()
    # def checkwishlistCheckout(self):
    #     self.checkwishlistCheckoutElement

class ProductPage:
    addtoCartId = ".single_add_to_cart_button"
    def __init__(self, driver):
        self.driver = driver
        self.addtocartElement = self.driver.find_element_by_css_selector(self.addtoCartId)

    # Adding product to Cart
    def addToCartProductPageMethod(self):
        self.addtocartElement.click()



class AddAddressCheckout:
    mascardId = "#MC"
    credcardId = "#wc-authorize-net-cim-credit-card-account-number"
    cardholderId = "#wc-authorize-net-cim-credit-card-holder-name"
    CVVId = "#wc-authorize-net-cim-credit-card-csc"
    addressId = ".add-new-address-icon-wrapper"
    firstNameId = "#billing_first_name"
    lastNameId = "#billing_last_name"
    companyId = "#billing_company"
    billingaddressId = "#billing_address_1"
    cityId = "#billing_city"
    stateId = "#billing_state_field > span:nth-child(3) > span:nth-child(1) > span:nth-child(1)"
    zipcodeId = "#billing_postcode"
    addpaymentId = "#wc-authorize-net-cim-credit-card-credit-card-form > div > div.column.small-12 > div > div.column.small-12.add-address-form > div > div:nth-child(7) > button"
    savePaymentbuttonCheckout = "div.small-12:nth-child(7) > button:nth-child(1)"
    addNewPaymentCheckoutId = ".payment-row-box > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)"
    placeOrderId = "#place_order"

    def __init__(self, driver):
        self.driver = driver
        self.addaddressCheckoutIcon = self.driver.find_element_by_css_selector(self.addressId)
        self.firstNameCheckout = self.driver.find_element_by_css_selector(self.firstNameId)
        self.lastnameCheckout = self.driver.find_element_by_css_selector(self.lastNameId)
        self.companyElement = self.driver.find_element_by_css_selector(self.companyId)
        self.addressElement = self.driver.find_element_by_css_selector(self.billingaddressId)
        self.cityElement = self.driver.find_element_by_css_selector(self.cityId)
        self.stateElement = self.driver.find_element_by_css_selector(self.stateId)
        self.zipcodeElement = self.driver.find_element_by_css_selector(self.zipcodeId)
        self.AddAddressElementCheckout = self.driver.find_element_by_css_selector(self.savePaymentbuttonCheckout)
        self.mascard = self.driver.find_element_by_css_selector(self.mascardId)
        self.credcard = self.driver.find_element_by_css_selector(self.credcardId)
        self.cardholder = self.driver.find_element_by_css_selector(self.cardholderId)
        self.CVVElement = self.driver.find_element_by_css_selector(self.CVVId)
        self.savePaymentElement = self.driver.find_element_by_css_selector(self.addpaymentId)
        self.placeOrderElement = self.driver.find_element_by_css_selector(self.placeOrderId)


    # Click (+) button in Secure Checkout for Add Payment
    def addAddressIcon(self):
        self.addaddressCheckoutIcon.click()

    def add_address_checkout(self): # Add Address field for Add payment in Checkout
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

    # Fill value of credit card in Add New Payment first time in Secure Checkout
    def credit_card_checkout(self):
        self.mascard.click()
        self.credcard.clear()
        self.driver.execute_script(
            "document.querySelector('#wc-authorize-net-cim-credit-card-account-number').value=" + str(
                mastercard) + "")
        self.cardholder.send_keys("K Tester")
        self.CVVElement.send_keys(str(random.randint(111, 999)))

    # Click Button [Save Address] in Add Credit Card > Add Payment> Add New Address
    def addAddressCheckoutPayment(self):
        self.AddAddressElementCheckout.click()

    # Button [Save payment] for add second credit card in SC
    def savePayment(self):
        self.savePaymentElement.click()

    # def cancelWishlistButton(self):
    #     self.cancelwishlistButtonElement.click()
    def placeOrder(self):
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.placeOrderId))).click()

class chooseAddress:
    selectExistedAddressId = "//li[@class='select2-results__option select2-results__option--highlighted']"
    chooseAddressId = "#select2-new-card__address-container"
    def __init__(self,driver):
        self.driver =driver
        self.selectExistedAddressElement = self.driver.find_element_by_xpath(self.selectExistedAddressId)
        self.chooseAddressElement = self.driver.find_element_by_css_selector(self.chooseAddressId)

    def chooseAddressAddPayment(self):
        self.chooseAddressElement.click()
        self.selectExistedAddressElement.click()

class changePayment:
    changePaymentId = ".payment-row-box > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > button:nth-child(2)"
    def __init__(self,driver):
        self.driver = driver
        self.changePaymentElement =self.driver.find_element_by_css_selector(self.changePaymentId)
    def chagePaymentClickCheckout(self):
        self.changePaymentElement.click()

class addNewPaymentChekoutExisterPayment():
    addnewpayment= "div.column:nth-child(9) > div:nth-child(1) > button:nth-child(1)"
    def __init__(self,driver):
        self.driver=driver
        self.addnewpaymentElement=self.driver.find_element_by_css_selector(self.addnewpayment)
    def addNewPaymentCheckout(self):
        wait = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_css_selector(self.addnewpaymentElement)).click()

class Header:
    MyWishlistId = "div.link-column:nth-child(2) > a:nth-child(1)"
    MyOrdersId = "div.link-column:nth-child(1) > a:nth-child(1)"
    ByDepartmentId = ".department-menu-holder-2 > span:nth-child(1)"
    def __init__(self,driver):
        self.driver =driver
        self.MyWishlistElement= self.driver.find_element_by_css_selector(self.MyWishlistId)
        self.MyOrdersElement = self.driver.find_element_by_css_selector(self.MyOrdersId)
        self.ByDepartmentsElement =self.driver.find_element_by_css_selector(self.ByDepartmentId)

    def LoginUserHeader(self):
        if self.ByDepartmentsElement:
            print "By Department is visible"
            if self.MyOrdersElement:
                print "My Orders is visible"
                if self.MyWishlistElement:
                    print "My Wishlist is visible "
                else:
                    print "Header missed some view"


