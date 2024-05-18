# sleep()
# implicit
# explicit
from time import sleep

# //ul[@role='menu']/li/a/p[contains(text(),"Sales")]

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

wait_obj = WebDriverWait(driver, 10)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, 'login-button').click()
# sleep(3)
wait_obj.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="menu"]/li/a/p[contains(text(),"Sales")]')))

driver.find_element(By.XPATH, '//ul[@role="menu"]/li/a/p[contains(text(),"Sales")]').click()
# sleep(3)

wait_obj.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@role='menu']/li/a/p[contains(text(),'Sales')]/parent::a/following-sibling::ul/li/a/p")))

elems=driver.find_elements(By.XPATH,"//ul[@role='menu']/li/a/p[contains(text(),'Sales')]/parent::a/following-sibling::ul/li/a/p")
for ele in elems:
    print(ele.text)
