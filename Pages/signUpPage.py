from Locators.locators import Locators
from selenium.webdriver.common.by import By
import time
class SignUpPage():

    def __init__(self, driver):
        self.driver = driver
        self.select_gender_mr_field_id=Locators.select_gender_mr_field_id
        self.customer_first_name_field_id=Locators.customer_first_name_field_id
        self.customer_last_name_field_id=Locators.customer_last_name_field_id
        self.Create_email_field_id=Locators.Create_email_field_id
        self.password_field_id=Locators.password_field_id
        self.days_feild_id=Locators.days_feild_id
        self.months_feild_id=Locators.months_feild_id
        self.years_feild_id=Locators.years_feild_id
        self.first_name_field_id=Locators.first_name_field_id
        self.last_name_field_id=Locators.last_name_field_id
        self.company_feild_id=Locators.company_feild_id
        self.address_feild_id=Locators.address_feild_id
        self.address2_feild_id=Locators.address2_feild_id
        self.city_feild_id=Locators.city_feild_id
        self.state_feild_id = Locators.state_feild_id
        self.postcode_feild_id = Locators.postcode_feild_id
        self.country_feild_id = Locators.country_feild_id
        self.other_feild_id = Locators.other_feild_id
        self.phone_feild_id = Locators.phone_feild_id
        self.phone_mobile_feild_id = Locators.phone_mobile_feild_id
        self.alias_feild_id = Locators.alias_feild_id
        self.submit_button_id = Locators.submit_button_id        


    def enter_id_gender(self):
        self.driver.find_element(By.ID, self.select_gender_mr_field_id).click()

    def enter_customer_first_name(self, customer_first_name):
        self.driver.find_element(By.ID, self.customer_first_name_field_id).send_keys(customer_first_name)

    def enter_customer_last_name(self, customer_last_name):
        self.driver.find_element(By.ID, self.customer_last_name_field_id).send_keys(customer_last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.Create_email_field_id).clear()
        self.driver.find_element(By.ID, self.Create_email_field_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def enter_days(self, days):
        self.driver.find_element(By.ID, self.days_feild_id).send_keys(days)

    def enter_months(self, months):
        self.driver.find_element(By.ID, self.months_feild_id).send_keys(months)

    def enter_years(self, years):
        self.driver.find_element(By.ID, self.years_feild_id).send_keys(years)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name)

    def enter_company(self, company):
        self.driver.find_element(By.ID, self.company_feild_id).send_keys(company)

    def enter_address(self, address):
        self.driver.find_element(By.ID, self.address_feild_id).send_keys(address)

    def enter_address2(self, address2):
        self.driver.find_element(By.ID, self.address2_feild_id).send_keys(address2)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.city_feild_id).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(By.ID, self.state_feild_id).send_keys(state)

    def enter_postcode(self, postcode):
        self.driver.find_element(By.ID, self.postcode_feild_id).send_keys(postcode)

    def enter_country(self, country):
        self.driver.find_element(By.ID, self.country_feild_id).send_keys(country)

    def enter_other(self, other):
        self.driver.find_element(By.ID, self.other_feild_id).send_keys(other)

    def enter_phone(self, phone):
        self.driver.find_element(By.ID, self.phone_feild_id).send_keys(phone)

    def enter_phone_mobile(self, phone_mobile): 
        self.driver.find_element(By.ID, self.phone_mobile_feild_id).send_keys(phone_mobile)

    def enter_alias(self, alias):
        self.driver.find_element(By.ID, self.alias_feild_id).send_keys(alias)

    def click_submit_button(self):
        self.driver.find_element(By.ID, self.submit_button_id).click()
        time.sleep(20)

""" driver.find_element(By.ID, "customer_lastname").send_keys("Qup")
driver.find_element(By.ID, "passwd").send_keys("123456789")
driver.find_element(By.ID, "days").send_keys("1")
driver.find_element(By.ID, "months").send_keys("January")
driver.find_element(By.ID, "years").send_keys("1997")
driver.find_element(By.ID, "company").send_keys("Qup")
driver.find_element(By.ID, "address1").send_keys("Qup")
driver.find_element(By.ID, "address2").send_keys("Qup")
driver.find_element(By.ID, "city").send_keys("Qup")
driver.find_element(By.ID, "id_state").send_keys("Alaska")
driver.find_element(By.ID, "postcode").send_keys("10001")
driver.find_element(By.ID, "id_country").send_keys("United States")
driver.find_element(By.ID, "other").send_keys("Qup")
driver.find_element(By.ID, "phone").send_keys("01234567890")
driver.find_element(By.ID, "phone_mobile").send_keys("01324567890")
driver.find_element(By.ID, "alias").send_keys("Qup")
driver.find_element(By.ID, "submitAccount").click()   """ 