import unittest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import TestHelper
import Registration


class VipOutletTestCheckout(unittest.TestCase):
    def __init__(self,driver):
        self.driver = driver
    def testCheckout(self):
        register = Registration.Registration(self.driver)
        register.test_register()
        while True:
            try:
                header =TestHelper.Header(self.driver)
                header.LoginUserHeader()
            except NoSuchElementException: print "Checking Header"
            else: break
        addproduct = TestHelper.addproductOnHomePage(self.driver)
        addproduct.productOnHomePage()
        while False:
            try:
                assert "[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product" in self.driver.page_source
            except NoSuchElementException:
                print "Can't add product to cart for first time user -[E14] Product Is Already Added To Your Shopping Cart. You Have Reached Quantity Limit For This Product "
                self.driver.close()
            else:
                print "Autotest over"
                break
        while True:
            try:
                addtocart = TestHelper.ProductPage(self.driver)
                addtocart.addToCartProductPageMethod()
            except NoSuchElementException,e:
                print "Click button [Add to Cart] on product page"
            else:
                break
        checkout = TestHelper.CheckoutPage(self.driver)
        # while True:
        #     try:
        #         checkout.addtoWishlistCheckoutElement()
        #     except NoSuchElementException:
        #         print "Click [Add to Wishlist] button"
        #     else:
        #         break
        # if checkout.checkwishlistCheckout:
        #     if (checkout.checkwishlistCheckout.text == 1):
        #         print "Wishlist"+checkout.checkwishlistCheckout.text+"Product is Added to Wishlist"
        # else:
        #     print "Product is not added to Wishlist - Fail"
        while True:
            try:
                checkout.addNewPaymentCheckout()
            except WebDriverException,e:
                print "Unable to click Add Payment in Checkout, retrying"
            else:
                break
        checkoutAddress = TestHelper.AddAddressCheckout(self.driver)
        checkoutAddress.credit_card_checkout()
        checkoutAddress.addAddressIcon()
        checkoutAddress.add_address_checkout()
        checkoutAddress.addAddressCheckoutPayment()


