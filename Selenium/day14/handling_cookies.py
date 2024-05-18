from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# location=r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day14"

#####chrome
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
ops = webdriver.ChromeOptions()
# ops.add_argument("--headless")
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_obj, options=ops)

driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
driver.implicitly_wait(10)

print(driver.get_cookies())

# [{'domain': 'admin-demo.nopcommerce.com', 'httpOnly': True, 'name': '.Nop.Antiforgery', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': 'CfDJ8IiSoo1ocrtFvurdsk63e1R_OT2XjLFEpdOTED4bBkDd38X26uhk0WgylPsa3p_d2mEqt2tyD-I7IYhHs4qX_aqEttC37COyPntSCaGwyO9oVaYK2dFLKxEb88qC6F2fMdb4gD2ryctCE9CdvnAsXqw'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1744023936, 'httpOnly': False, 'name': '.Nop.Culture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c%3Den-US%7Cuic%3Den-US'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1744023936, 'httpOnly': True, 'name': '.Nop.Customer', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '74e707d3-bcd7-49ef-ae77-050fa300546e'}]


driver.add_cookie({'name':"mycookie", "value":"123456"})
print(driver.get_cookies())

# print(driver.get_cookie("mycookie"))
# for c in driver.get_cookies():
#     print(c['name'])
#

# delete signle cookie

# driver.delete_cookie("mycookie")
# for c in driver.get_cookies():
#     print(c['name'])
#
# delete all cookies

driver.delete_all_cookies()

for c in driver.get_cookies():
    print(c['name'])