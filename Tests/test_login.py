from lib2to3.pgen2 import driver
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import sys
import os
import HtmlTestRunner
import test_signup

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
from Pages.myAccount import myAccount
#from Locators.locators import Locators

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.common.by import By
        import time
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login_1(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        Index_page= IndexPage(driver)
        Index_page.click_sign_in()

        login_page = LoginPage(driver)
        login_page.enter_username("siam.qups@gmail.com")
        login_page.enter_password("123456789")
        login_page.click_login()

        #home_page = HomePage(driver)
        

        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/codes/bs23/POM/reports'))








