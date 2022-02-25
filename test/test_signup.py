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
from Pages.signUpPage import SignUpPage


class SignupTest(unittest.TestCase):

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

    def test_valid_signup_1(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        
        #Index Page
        Index_page= IndexPage(driver)
        Index_page.click_sign_in()

        #Login Page
        login_page = LoginPage(driver)
        login_page.click_register(loginEmail1)

        #Signup Page
        signup_page = SignUpPage(driver)
        signup_page.enter_id_gender()
        signup_page.enter_customer_first_name("Siam")
        signup_page.enter_customer_last_name("Qups")
        signup_page.enter_email(loginEmail1)
        signup_page.enter_password("123456789")
        signup_page.enter_days("1")
        signup_page.enter_months("January")
        signup_page.enter_years("1997")
        signup_page.enter_first_name("Siam")
        signup_page.enter_last_name("Qups")
        signup_page.enter_company("Siam Industries")
        signup_page.enter_address("qups")
        signup_page.enter_address2("qups2")
        signup_page.enter_city("dhaka")
        signup_page.enter_state("Alaska")
        signup_page.enter_postcode("10001")
        signup_page.enter_country("United States")
        signup_page.enter_other("qups")
        signup_page.enter_phone("01234567890")
        signup_page.enter_phone_mobile("01234567890")
        signup_page.enter_alias("qups")
        signup_page.click_submit_button()
        signup_page.click_signout_button()

    
    def test_valid_signup_2(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        Index_page= IndexPage(driver)
        Index_page.click_sign_in()

        login_page = LoginPage(driver)
        login_page.click_register(loginEmail2)

        signup_page = SignUpPage(driver)
        signup_page.enter_id_gender()
        signup_page.enter_customer_first_name("Siam")
        signup_page.enter_customer_last_name("Qups")
        signup_page.enter_email(loginEmail2)
        signup_page.enter_password("123456789")
        signup_page.enter_days("1")
        signup_page.enter_months("January")
        signup_page.enter_years("1997")
        signup_page.enter_first_name("Siam")
        signup_page.enter_last_name("Qups")
        signup_page.enter_company("Siam Industries")
        signup_page.enter_address("qups")
        signup_page.enter_address2("qups2")
        signup_page.enter_city("dhaka")
        signup_page.enter_state("Alaska")
        signup_page.enter_postcode("10001")
        signup_page.enter_country("United States")
        signup_page.enter_other("qups")
        signup_page.enter_phone("01234567890")
        signup_page.enter_phone_mobile("01234567890")
        signup_page.enter_alias("qups")
        signup_page.click_submit_button()
        signup_page.click_signout_button()

        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test signup Completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/codes/bs23/POM/reports'))

###################################################
##############COMMAND TO RUN TEST##################
# python -m unittest