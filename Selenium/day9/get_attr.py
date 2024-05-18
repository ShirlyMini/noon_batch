from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# print(driver.find_element(By.ID, "Email").get_attribute("data-val-email"))
# print(driver.find_element(By.ID, "Email").get_attribute("name"))
# print(driver.find_element(By.ID, "Email").get_attribute("value"))
# print(driver.find_element(By.ID, "Password").get_attribute("value"))
#
#
# # driver.find_element(By.ID, "Email").clear()
# # driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
# # driver.find_element(By.ID, "Password").clear()
# # driver.find_element(By.ID, "Password").send_keys("admin")

driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.find_element(By.ID, "email").get_attribute("value"))
driver.find_element(By.ID, "email").send_keys("usename")
print(driver.find_element(By.ID, "email").get_attribute("value"))


print(driver.find_element(By.ID, "pass").get_attribute("value"))
driver.find_element(By.ID, "pass").send_keys("abcdef")
print(driver.find_element(By.ID, "pass").get_attribute("value"))

sleep(5)