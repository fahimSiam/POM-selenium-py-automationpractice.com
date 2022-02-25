from Locators.locators import Locators
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Products():

    def __init__(self, driver):
        self.driver = driver
        self.act_chains=ActionChains(driver)
        self.casual_dresses_link_text = Locators.casual_dresses_link_text
        self.casual_dress_add_to_cart = Locators.casual_dress_add_to_cart
        self.continue_shop_button_xpath= Locators.continue_shop_button_xpath
        self.Tshirt_section_xpath = Locators.Tshirt_section_xpath
        self.filter_blue_xpath = Locators.filter_blue_xpath
        self.blue_tshirt_add_to_cart = Locators.blue_tshirt_add_to_cart
        self.proceed_to_checkout_button_xpath = Locators.proceed_to_checkout_button_xpath
        self.dress_item = Locators.dress_item
        self.blue_tshirt_item = Locators.blue_tshirt_item
    def click_casual_dresses(self):
        self.driver.find_element(By.LINK_TEXT, self.casual_dresses_link_text).click()
    
    def click_add_to_cart(self):
        dress=self.driver.find_element(By.XPATH, self.dress_item)
        self.act_chains.move_to_element(dress).perform()
        self.driver.find_element(By.XPATH, self.casual_dress_add_to_cart).click()

    def click_continue_shop(self):
        self.driver.find_element(By.XPATH, self.continue_shop_button_xpath).click()
    
    def click_Tshirt_section(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Tshirt_section_xpath).click()
    
    def click_filter_blue(self):
        self.driver.find_element(By.XPATH, self.filter_blue_xpath).click()

    def click_add_to_cart_blue(self):
        blueTshirt=self.driver.find_element(By.XPATH, self.blue_tshirt_item)
        self.act_chains.move_to_element(blueTshirt).perform()
        self.driver.find_element(By.XPATH, self.blue_tshirt_add_to_cart).click()
    
    def click_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, self.proceed_to_checkout_button_xpath).click()

