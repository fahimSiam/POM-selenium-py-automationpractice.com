from Locators.locators import Locators
from selenium.webdriver.common.by import By
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_field_xpath = Locators.email_field_xpath
        self.password_field_id = Locators.password_field_id
        self.submit_button_id = Locators.submit_Login_button_id
        self.submit_register_button_id = Locators.submit_register_button_id
        self.register_email_field_id= Locators.register_email_field_id


    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(username)
    
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.submit_button_id).click()
        #time.sleep(20)

    def click_register(self, register_email):
        self.driver.find_element(By.ID, self.register_email_field_id).clear()
        self.driver.find_element(By.ID, self.register_email_field_id).send_keys(register_email)
        self.driver.find_element(By.ID, self.submit_register_button_id).click()
