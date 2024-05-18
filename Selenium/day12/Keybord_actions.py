from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://jqueryui.com/autocomplete/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

##################seletcing random element
# driver.find_element(By.ID, "tags").send_keys("a")
# driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
# sleep(2)
# driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
# sleep(2)
# driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
# print(driver.find_element(By.ID, "tags").get_attribute("value"))

##################seletcing particualr element

driver.find_element(By.ID, "tags").send_keys("a")

while True:
    driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
    option = driver.find_element(By.ID, "tags").get_attribute("value")
    if option=="Java":
        driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
        break
    sleep(2)

print(driver.find_element(By.ID, "tags").get_attribute("value"))
sleep(10)