from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

#############abs xptha

# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").clear()
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").send_keys("admin@yourstore.com")
#
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").clear()
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").send_keys("admin")
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


####################relactive
#//tag[@attr="value"]

driver.find_element(By.XPATH, "//input[@type='email']").clear()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(10)

