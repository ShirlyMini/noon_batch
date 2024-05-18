from time import sleep
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# location=r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day14"

#####chrome
# service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
# preferences={"download.default_directory":location}
# ops = webdriver.ChromeOptions()
# ops.add_experimental_option("prefs", preferences)
# driver = webdriver.Chrome(service=service_obj, options=ops)
#

####edge
# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# preferences={"download.default_directory":location}
# ops = webdriver.EdgeOptions()
# ops.add_experimental_option("prefs", preferences)
# driver = webdriver.Edge(service=service_obj, options=ops)

####firefox
# # service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# preferences={"download.default_directory":location}
# ops = webdriver.FirefoxOptions()
# ops.set_preference("browser.download.folderList",2)##0-desktop,1-download folder(default),2-desiredloc
# ops.set_preference("browser.download.dir",location)
# driver = webdriver.Firefox( options=ops)
#
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.find_element(By.NAME, "Email").clear()
# driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME, "Password").clear()
# driver.find_element(By.NAME, "Password").send_keys("admin")
# driver.find_element(By.TAG_NAME, 'button').click()
# sleep(3)
# driver.find_element(By.XPATH,"//ul[@role='menu']/li/a/p[contains(text(),'Sales')]").click()
# sleep(2)
# driver.find_element(By.XPATH,"//ul[@role='menu']/li/ul/li/a/p[text()=' Orders']").click()
# driver.find_element(By.XPATH,"//button[@class='btn btn-success dropdown-toggle dropdown-icon']").click()
# sleep(3)
# driver.find_element(By.XPATH,"//button[@name='exportexcel-all']").click()
# sleep(10)


#######################3
# import os
# os.copy_file_range()