from Locators.locators import Locators
from selenium.webdriver.common.by import By

class IndexPage():

    def __init__(self, driver):
        self.driver = driver
        self.click_sign_in_partial_link_text = Locators.click_sign_in_partial_link_text
    

    def click_sign_in(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.click_sign_in_partial_link_text).click()

        