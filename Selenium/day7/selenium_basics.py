from time import sleep

from selenium import webdriver


from selenium.webdriver.chrome.service import Service
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")#(used to connect with webdriver)
driver = webdriver.Chrome(service=service_obj)#(launching browser)
##(or)
# driver = webdriver.Chrome()

# ############edge
# from selenium.webdriver.edge.service import Service
# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)
# # driver = webdriver.Edge()

############ff
# from selenium.webdriver.firefox.service import Service
# # service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
# # driver = webdriver.Firefox(service=service_obj)
# driver = webdriver.Firefox()

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
#
print(driver.title)
print(driver.current_url)
print(driver.page_source)
# navigator
driver.refresh()
driver.back()
driver.forward()
sleep(5)