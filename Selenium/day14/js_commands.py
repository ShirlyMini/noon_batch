from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.execute_script("document.getElementById('Email').value=''")
# driver.execute_script("document.getElementById('Email').value='admin@yourstore.com'")
# driver.execute_script("document.getElementById('Password').value=''")
# driver.execute_script("document.getElementById('Password').value='admin'")
#
# we = driver.find_element(By.CLASS_NAME, 'login-button')
# driver.execute_script("arguments[0].click()", we)
#
# sleep(10)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
sleep(20)
#scrolltooffset
# driver.execute_script("window.scrollBy(0,3000)")
# print(driver.execute_script("return window.pageYOffset;"))
# print(driver.execute_script("return window.pageXOffset;"))
# #scrolluntilelementfound
# flag=driver.find_element(By.XPATH,'//img[@alt="Flag of India"]')
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# sleep(3)
# print(driver.execute_script("return window.pageYOffset;"))
# print(driver.execute_script("return window.pageXOffset;"))
# #scrolltoendofpage
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
print(driver.execute_script("return window.pageYOffset;"))
print(driver.execute_script("return window.pageXOffset;"))
sleep(5)
# #scrollbacktotopofpage
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
print(driver.execute_script("return window.pageYOffset;"))
print(driver.execute_script("return window.pageXOffset;"))