from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchBy:
    id_email="SearchEmail"
    id_fname="SearchFirstName"
    id_lname="SearchLastName"
    id_search_button="search-customers"
    xpath_verify_email="//table[@id='customers-grid']/tbody/tr/td[2]"
    xpath_verify_name="//table[@id='customers-grid']/tbody/tr/td[3]"

    def __init__(self, driver):
        self.driver=driver

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetFirstName(self, name):
        self.driver.find_element(By.ID, self.id_fname).send_keys(name)

    def SetLastName(self, name):
        self.driver.find_element(By.ID, self.id_lname).send_keys(name)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.id_search_button).click()

    def VerifyEmailSearch(self):
        return self.driver.find_element(By.XPATH, self.xpath_verify_email).text

    def VerifyNameSearch(self, name):
        list_of_webelem =  self.driver.find_elements(By.XPATH, self.xpath_verify_name)
        for elem in list_of_webelem:
            if name in elem.text:
                continue
            else:
                return False
        return True