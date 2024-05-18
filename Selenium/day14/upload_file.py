from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# location=r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day14"

#####chrome
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.TAG_NAME, 'button').click()
sleep(3)
driver.find_element(By.XPATH,"//ul[@role='menu']/li/a/p[contains(text(),'Sales')]").click()
sleep(2)
driver.find_element(By.XPATH,"//ul[@role='menu']/li/ul/li/a/p[text()=' Orders']").click()
driver.find_element(By.NAME,"importexcel").click()
sleep(3)
driver.find_element(By.NAME,"importexcelfile").send_keys(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day14\orders.xlsx")

sleep(10)
