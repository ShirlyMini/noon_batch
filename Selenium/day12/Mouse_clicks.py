from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
###########right Click#####
# act_obj = ActionChains(driver)
# r_clk_elem=driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
# act_obj.context_click(r_clk_elem).perform()
# option_clk_ele=driver.find_element(By.XPATH, "//span[contains(text(),'Copy')]")
# act_obj.move_to_element(option_clk_ele).click().perform()
#
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)
# alt_obj.accept()


########################double click

act_obj = ActionChains(driver)
d_clk_elem = driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")
act_obj.double_click(d_clk_elem).perform()

alt_obj = driver.switch_to.alert
print(alt_obj.text)
alt_obj.accept()

sleep(10)