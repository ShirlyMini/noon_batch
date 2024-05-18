from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)

######navigator commands

# driver.refresh()
# driver.get("https://www.facebook.com/")
# print(driver.title)
# driver.back()
# print(driver.title)
# driver.forward()
# print(driver.title)

##########browser command

driver.close()# close the curent browser-driver focuse
driver.quit()# terminate all the browser process