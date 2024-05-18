from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.linkedin.com/learning-login")
# driver.maximize_window()
#
# print(driver.find_element(By.ID, "auth-id-button").is_displayed())
# print(driver.find_element(By.ID, "auth-id-button").is_enabled())
# driver.find_element(By.ID, "auth-id-input").send_keys("name")
# print(driver.find_element(By.ID, "auth-id-button").is_enabled())


driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

print(driver.find_element(By.ID, "RememberMe").is_selected())
driver.find_element(By.ID, "RememberMe").click()
print(driver.find_element(By.ID, "RememberMe").is_selected())

#https://www.facebook.com/signup
#https://demoqa.com/checkbox