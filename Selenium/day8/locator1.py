# normal-id, name, class, tag, linktext and partial link text

#########################3id

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()

# driver.find_element(By.ID, "Email").clear()
# driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID, "Password").clear()
# driver.find_element(By.ID, "Password").send_keys("admin")

#####################name
# driver.find_element(By.NAME, "Email").clear()
# driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME, "Password").clear()
# driver.find_element(By.NAME, "Password").send_keys("admin")

#########################tag
# driver.find_element(By.TAG_NAME, 'button').click()
#########################class
# driver.find_element(By.CLASS_NAME, 'login-button').click()


driver.get("https://www.facebook.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Create new account").click()

sleep(10)