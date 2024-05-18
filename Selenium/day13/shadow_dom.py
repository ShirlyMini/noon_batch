##
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

####signle shadow root
# driver.get("https://books-pwakit.appspot.com/")
#
# shadowroot_1 = driver.find_element(By.CSS_SELECTOR, "book-app").shadow_root
# shadowroot_1.find_element(By.ID, "input").send_keys("Harry Potter")


####multiple shadow root
driver.get("chrome://settings/downloads")
shadow_1 = driver.find_element(By.CSS_SELECTOR, "settings-ui").shadow_root
shadow_2 = shadow_1.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root
shadow_3 = shadow_2.find_element(By.CSS_SELECTOR, "settings-basic-page.cr-centered-card-container").shadow_root
shadow_4 = shadow_3.find_element(By.CSS_SELECTOR, "settings-downloads-page").shadow_root
shadow_5 = shadow_4.find_element(By.CSS_SELECTOR, "settings-toggle-button.hr").shadow_root
print(shadow_5.find_element(By.CSS_SELECTOR, "div.label").text)

sleep(5)