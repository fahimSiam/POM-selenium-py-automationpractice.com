from Locators.locators import Locators
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Checkout():

    def __init__(self, driver):
        self.driver = driver
        self.act_chains=ActionChains(driver)
        self.summary_proceed_to_checkout=Locators.summary_proceed_to_checkout
        self.address_proceed_to_checkout_button_xpath=Locators.address_proceed_to_checkout_button_xpath
        self.shipping_proceed_to_checkout_button_xpath=Locators.shipping_proceed_to_checkout_button_xpath
        self.shipping_agree_to_terms_checkbox_id=Locators.shipping_agree_to_terms_checkbox_id
        self.pay_by_check_partial_link_text=Locators.pay_by_check_partial_link_text
        self.signout_partial_link_text=Locators.signout_partial_link_text
        self.total_price_xpath=Locators.total_price_xpath

    def click_summary_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, self.summary_proceed_to_checkout).click()

    def click_address_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, self.address_proceed_to_checkout_button_xpath).click()

    def click_shipping_proceed_to_checkout(self):
        self.driver.find_element(By.ID, self.shipping_agree_to_terms_checkbox_id).click()
        self.driver.find_element(By.XPATH, self.shipping_proceed_to_checkout_button_xpath).click()
    
    def click_pay_by_check(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.pay_by_check_partial_link_text).click()

    def click_signout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.signout_partial_link_text).click()
        time.sleep(15)

    def print_total_price(self):
        total_price = self.driver.find_element(By.XPATH, Locators.total_price_xpath).text
        print("THE TOTAL PRICE IS: "+total_price)
