from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# print(driver.window_handles)#[parent]
# driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
#
# print(driver.window_handles)#[parent, child1, child2]
#
# for i in driver.window_handles[1:]:
#     driver.switch_to.window(i)
#     print(driver.title)
#
# # # driver.close()#---driver focus
# # driver.quit()#terminate the browser process
# sleep(20)

driver.get("https://www.myntra.com/tops")
driver.maximize_window()

driver.find_element(By.XPATH, "//ul[@class='results-base']/li[1]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[2]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[3]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[4]").click()

for i in driver.window_handles[1:]:
    driver.switch_to.window(i)
    print(driver.find_element(By.XPATH,"//span[@class='pdp-price']/strong").text)
    driver.close()

driver.quit()