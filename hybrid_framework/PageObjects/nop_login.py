from selenium.webdriver.common.by import By


class login:
    id_username="Email"
    id_password="Password"
    xpath_login="//button[@type='submit']"

):
        self.driver = driver

    def SetEmail(    def __init__(self, driverself, email):
        self.driver.find_element(By.ID, self.id_username).clear()
        self.driver.find_element(By.ID, self.id_username).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.id_password).clear()
        self.driver.find_element(By.ID, self.id_password).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()