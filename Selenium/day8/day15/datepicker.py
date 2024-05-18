# import datetime
# dt1=datetime.datetime.now()#2024-04-13 15:51:57.795487
# print(dt1.strftime("%B, %d, %Y")) #April, 13, 2024
# print(dt1.strftime("%b, %d, %y")) #April, 13, 2024
# print(dt1.strftime("%b, %d, %y %H %M %S %p")) #April, 13, 2024
import datetime
## 14/04/2023

#year mon date hrs min sec ms
# dt2=datetime.datetime(1999, 4,14, 5, 45,12)
# print(dt2.strftime("%B, %d, %Y")) #April, 13, 2024
# print(dt2.strftime("%b, %d, %y")) #April, 13, 2024
# print(dt2.strftime("%b-%d-%y")) #April, 13, 2024
# print(dt2.strftime("%b/%d/%y")) #April, 13, 2024
# print(dt2.strftime("%b, %d, %y %H %M %S %p")) #April, 13, 2024


##############################################################################

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
ops = webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_obj, options=ops)

driver.get("https://demo.automationtesting.in/Datepicker.html")


#######date picker enables
# dt1=datetime.datetime(2025,4,14)
# print(dt1.strftime("%m/%d/%Y"))
#
# driver.find_element(By.ID, "datepicker2").send_keys(dt1.strftime("%m/%d/%Y"))
# if driver.find_element(By.ID, "datepicker2").get_attribute("value") == dt1.strftime("%m/%d/%Y"):
#     print("date ented successfully ", driver.find_element(By.ID, "datepicker2").get_attribute("value"))
#
# sleep(10)

#######date picker disable
# def func1(y,m,d):
#
#     dt1=datetime.datetime(y,m,d)
#     # print(dt1.strftime("%m/%d/%Y"))
#     month = dt1.strftime("%B")
#     year = dt1.strftime("%Y")
#     d1 = dt1.strftime("%d").lstrip("0")# with zero padding
#
#     driver.find_element(By.ID, "datepicker2").click()
#     month_drpdown = Select(driver.find_element(By.XPATH, "//select[@title='Change the month']"))
#     month_drpdown.select_by_visible_text(month)
#     year_drpdown = Select(driver.find_element(By.XPATH, "//select[@title='Change the year']"))
#     year_drpdown.select_by_visible_text(year)
#     driver.find_element(By.XPATH, f"//div[@class='datepick-month']/table/tbody/tr/td/a[text()='{d1}']").click()
#
#     if driver.find_element(By.ID, "datepicker2").get_attribute("value") == dt1.strftime("%m/%d/%Y"):
#         print("date entered successfully ", driver.find_element(By.ID, "datepicker2").get_attribute("value"))
#
#     sleep(10)
#
# func1(2015,12,12)

#####using navigator

dt1=datetime.datetime(2022, 12, 25)
print(dt1.strftime("%m/%d/%Y"))
month = dt1.strftime("%B")
year = dt1.strftime("%Y")
d1 = dt1.strftime("%d").lstrip("0")# with zero padding

#//span[@class='ui-datepicker-month']
#//span[@class='ui-datepicker-year']
#//a[@title='Prev']
#//a[@title='Next']
driver.find_element(By.ID, "datepicker1").click()
while True:
    if int(driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text) > int(year):
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
    elif int(driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text) < int(year):
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
    elif int(driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text) == int(year):
        break
    else:
        break
    sleep(2)

cal_month={"January":1,
           "February":2,
           "March":3,
           "April":4,
           "May":5,
           "June":6,
           "July":7,
           "August":8,
           "September":9,
           "October":10,
           "November":11,
           "December":12,
           }

while True:
    month_ui = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    if cal_month[month_ui]<int(dt1.strftime("%m")):
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
    elif cal_month[month_ui]>int(dt1.strftime("%m")):
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
    elif cal_month[month_ui]==int(dt1.strftime("%m")):
        break
    else:
        break
    sleep(2)

driver.find_element(By.XPATH, f"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()='{d1}']").click()

if driver.find_element(By.ID, "datepicker1").get_attribute("value") == dt1.strftime("%m/%d/%Y"):
    print("date entered successfully ", driver.find_element(By.ID, "datepicker1").get_attribute("value"))
sleep(10)