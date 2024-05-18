from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
sleep(20)
act_obj = ActionChains(driver)
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# act_obj.scroll_to_element(flag).perform()

# act_obj.scroll_by_amount(0,2000).perform()

flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
sc_orgn = ScrollOrigin.from_element(flag)

act_obj.scroll_from_origin(sc_orgn, 0, 1000).perform()

sleep(10)