import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(4)

######################
# by class name
# driver.find_element(By.CLASS_NAME, "button-1").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)
#
# driver.find_element(By.CLASS_NAME, "login-button").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)
#
# # by tagname
# driver.find_element(By.TAG_NAME, "button").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)

#################### why link text and partial link text for login is not working?????????
# by link text# a
# driver.find_element(By.LINK_TEXT, "Log in").click()# invalid
# driver.find_element(By.LINK_TEXT, "Logout").click()
# time.sleep(2)
#
# # by partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()# invalid
# driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
# time.sleep(2)

######################
# by css selector
# driver.find_element(By.CSS_SELECTOR, "button.button-1").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "button.login-button").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href= '/logout']").click()
# time.sleep(2)

####################### Why below selectors for class are not working?????????????????
# driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, "button[class='login-button']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "button[class='login-button']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
# time.sleep(2)


######################
# # by absolute xpath
# driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "html/body/div[3]/nav/div/ul/li[3]/a").click()
# time.sleep(2)
#
# # by relative xpath
# driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[@href= '/logout']").click()
# time.sleep(2)

####################### Why below relative xpath with class are not working?????????????????
driver.find_element(By.XPATH, "//*[@class='button-1 login-button']").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
time.sleep(2)

# driver.find_element(By.XPATH, "//*[@class='login-button']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//*[@class='button-1.login-button']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
# time.sleep(2)
# #######################

# # with contains(text())
# driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
# time.sleep(2)
#
# # with text()
# driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[text()= 'Logout']").click()
# time.sleep(2)
#
# # starts-with()
# driver.find_element(By.XPATH, "//button[starts-with(text(), 'Log in')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[starts-with(text(), 'Logout')]").click()
# time.sleep(2)

