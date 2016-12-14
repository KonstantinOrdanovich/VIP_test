from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException

testemail = ("acyll"+str(random.randint(2000,7000))+"@armyspy.com")
testemail2 = ("acyll" + str(random.randint(2000, 7000)) + "@armyspy.com")
testemail3 = "acyll1988@armyspy.com"
server = "https://uat.vipoutlet.com"


class testhelperclass:

    def email(self):
        email = self.driver.find_element_by_css_selector(
            "div.row > div:nth-child(1) > form:nth-child(2) > input:nth-child(3)")
        email.clear()
        email.send_keys(testemail2)
        password = self.driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test")
        terms = self.driver.find_element_by_css_selector(".box")
        terms.click()
        register = self.driver.find_element_by_name("register")
        register.click()
        print testemail2
        self.driver.close()
