from lib2to3.pgen2 import driver
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import sys
import os
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
from Pages.myAccount import MyAccount
from Pages.products import Products
from Pages.checkout import Checkout
from test.test_signup import SignupTest

class TotalTest(unittest.TestCase):
    global loginEmail1
    loginEmail1 = "siam.qups27@gmail.com"
    global loginEmail2
    loginEmail2 = "siam.qups28@gmail.com"
    
    @classmethod
    def setUpClass(cls):
        
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.common.by import By
        import time
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_checkout_1(self):
        
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        #Index Page
        Index_page= IndexPage(driver)
        Index_page.click_sign_in()

        #Login Page
        login_page = LoginPage(driver)
        login_page.enter_username(loginEmail1)
        login_page.enter_password("123456789")
        login_page.click_login()

        #My Account Page
        myaccount_page = MyAccount(driver)
        myaccount_page.click_dresses()

        #Products Page
        products_page = Products(driver)
        products_page.click_casual_dresses()
        products_page.click_add_to_cart()
        products_page.click_continue_shop()
        products_page.click_Tshirt_section()
        products_page.click_filter_blue()
        products_page.click_add_to_cart_blue()
        products_page.click_proceed_to_checkout()

        #Checkout Page
        checkout_page = Checkout(driver)
        checkout_page.click_summary_proceed_to_checkout()
        checkout_page.click_address_proceed_to_checkout()
        checkout_page.click_shipping_proceed_to_checkout()
        checkout_page.print_total_price()
        checkout_page.click_pay_by_check()
        checkout_page.click_signout()


    def test_login_checkout_2(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        #Index Page
        Index_page= IndexPage(driver)
        Index_page.click_sign_in()

        #Login Page
        login_page = LoginPage(driver)
        login_page.enter_username(loginEmail2)
        login_page.enter_password("123456789")
        login_page.click_login()

        #My Account Page
        myaccount_page = MyAccount(driver)
        myaccount_page.click_dresses()

        #Products Page
        products_page = Products(driver)
        products_page.click_casual_dresses()
        products_page.click_add_to_cart()
        products_page.click_continue_shop()
        products_page.click_Tshirt_section()
        products_page.click_filter_blue()
        products_page.click_add_to_cart_blue()
        products_page.click_proceed_to_checkout()

        #Checkout Page
        checkout_page = Checkout(driver)
        checkout_page.click_summary_proceed_to_checkout()
        checkout_page.click_address_proceed_to_checkout()
        checkout_page.click_shipping_proceed_to_checkout()
        checkout_page.print_total_price()
        checkout_page.click_pay_by_check()
        checkout_page.click_signout()
            

        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/codes/bs23/POM/reports'))








