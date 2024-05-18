
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

########################findelemnets vs find element

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
##### FIND_ELEMENT
######## loc matching single web elem

# driver.find_element(By.XPATH,"//a[contains(text(),'Force Motors')]").click()
# print(driver.title)

####### loc matching multiple web elem
# driver.find_element(By.XPATH, "//tbody/tr/td/a").click()
# print(driver.title)

#####with invalid locator
# driver.find_element(By.XPATH, "//sdfgdsfa").click()##selenium.common.exceptions.NoSuchElementException
# print(driver.title)

##### FIND_ELEMENTS
######## loc matching single web elem
# elem = driver.find_elements(By.XPATH,"//a[contains(text(),'Force Motors')]")
# for ele in elem:
#     ele.click()
# print(driver.title)

####### loc matching multiple web elem
# elem = driver.find_elements(By.XPATH,"//tbody/tr/td/a")
# for ele in elem:
#     print(ele.text)

#####with invalid locator
print(driver.find_elements(By.XPATH, "//sdfgdsfa"))
# print(driver.title)

