# Custom locator
# 1 css
# 2 xpath

######CSS

# tag#valueofid
# tag.valueofclass
#tag[attr=value]

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
# tag#valueofid
driver.find_element(By.CSS_SELECTOR, "input#Email").clear()
driver.find_element(By.CSS_SELECTOR, "input#Email").send_keys("admin@yourstore.com")

# tag.valueofclass
driver.find_element(By.CSS_SELECTOR, "input.password").clear()
driver.find_element(By.CSS_SELECTOR, "input.password").send_keys("admin")

#tag[attr=value]
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

sleep(10)