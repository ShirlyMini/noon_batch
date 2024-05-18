from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

act_obj = ActionChains(driver)
act_obj.pause()

#####approach1
# course1_elem = driver.find_element(By.XPATH,"//span[text()='Courses']")
# course2_elem = driver.find_element(By.XPATH,"//span[text()='For Working Professionals']")
# course3_elem = driver.find_element(By.XPATH,"//a[contains(text(),'DevOps Engineering (LIVE)')]")
#
# act_obj.move_to_element(course1_elem).move_to_element(course2_elem).move_to_element(course3_elem).click().perform()

#####approach2
course1_elem = driver.find_element(By.XPATH,"//span[text()='Courses']")
act_obj.move_to_element(course1_elem).perform()
course2_elem = driver.find_element(By.XPATH,"//span[text()='For Working Professionals']")
act_obj.move_to_element(course2_elem).perform()
course3_elem = driver.find_element(By.XPATH,"//a[contains(text(),'DevOps Engineering (LIVE)')]")
act_obj.move_to_element(course3_elem).click().perform()

print(driver.title)
sleep(10)