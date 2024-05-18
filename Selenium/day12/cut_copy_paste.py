from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

driver.find_element(By.XPATH,"//li[@id='userProfileId']/a[text()='Sign In']").click()
sleep(3)
driver.find_element(By.XPATH,"//label[@for='tab2']").click()
driver.find_element(By.ID,"email").send_keys("abc@gmail.com")

############
act_obj=ActionChains(driver)
#ctrl+a and ctrl+c
act_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

###TAB
act_obj.send_keys(Keys.TAB).perform()
####Ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

###TAB
act_obj.send_keys(Keys.TAB).perform()
####Ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
