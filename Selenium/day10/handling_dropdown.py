from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")

#######################tag
driver.find_element(By.TAG_NAME, 'button').click()

##############type 1 drop down
driver.find_element(By.XPATH,"//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(2)
driver.find_element(By.XPATH,"//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()


#################select dowpdown
we_drpdowd=driver.find_element(By.NAME, "products-grid_length")
drp_obj = Select(we_drpdowd)
drp_obj.select_by_visible_text("100")
# sleep(2)
# drp_obj.select_by_value("7")
# sleep(2)
# drp_obj.select_by_index(1)#0 to n-1

##########click check based on condition
sleep(7)
row_count = driver.find_elements(By.XPATH,"//table[@id='products-grid']/tbody/tr/td[5]")

for r_count in range(1,len(row_count)+1):
    price=driver.find_element(By.XPATH,f"//table[@id='products-grid']/tbody/tr[{r_count}]/td[5]")
    if price.text!="":
        if float(price.text)>=1000:
            driver.find_element(By.XPATH, f"//table[@id='products-grid']/tbody/tr[{r_count}]/td[1]/input").click()
sleep(10)