from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

fr1_we=driver.find_element(By.XPATH,"/html/frameset/frame[1]")
driver.switch_to.frame(fr1_we)
driver.find_element(By.NAME, "mytext1").send_keys("frame1")

driver.switch_to.default_content()

fr2_we=driver.find_element(By.XPATH, "/html/frameset/frameset/frame[1]")
driver.switch_to.frame(fr2_we)
driver.find_element(By.NAME, "mytext2").send_keys("frame2")

driver.switch_to.default_content()

fr3_we=driver.find_element(By.XPATH, "/html/frameset/frameset/frame[2]")
driver.switch_to.frame(fr3_we)
driver.find_element(By.NAME, "mytext3").send_keys("frame3")

inner_fr_we = driver.find_element(By.XPATH,"//iframe")
driver.switch_to.frame(inner_fr_we)
driver.find_element(By.XPATH, "//div[@id='i5']").click()

driver.switch_to.parent_frame()

driver.find_element(By.NAME, "mytext3").clear()
driver.find_element(By.NAME, "mytext3").send_keys("after clicking radio button")


sleep(10)