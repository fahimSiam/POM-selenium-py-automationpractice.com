from Locators.locators import Locators
from selenium.webdriver.common.by import By
import time
class MyAccount():

    def __init__(self, driver):
        self.driver = driver
        self.dresses_xpath = Locators.dresses_xpath
        

    def click_dresses(self):
        self.driver.find_element(By.XPATH, self.dresses_xpath).click()
    