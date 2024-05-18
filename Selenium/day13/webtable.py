from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")

# spcific row or col
###col
# header_elem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/thead/tr/th")
#
# for indx in range(0,len(header_elem)):
#     print(header_elem[indx].text)
#     if header_elem[indx].text == "Prev Close (Rs)":
#         company_idx = indx
#
# print(company_idx)#0
#
#
# comp_list = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr/td[{company_idx}+1]")
# for comp in comp_list:
#     print(comp.text)

###### row

header_elem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/thead/tr/th")

for indx in range(0,len(header_elem)):
    print(header_elem[indx].text)
    if header_elem[indx].text == "Current Price (Rs)":
        idx = indx
    elif header_elem[indx].text == "Company":
        c_idx = indx

print(c_idx,idx)#0


row_elem = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr")#2319

for row in range(1, len(row_elem)+1):
    cur_price = float(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row}]/td[{idx + 1}]").text.replace(",",""))
    if  cur_price <=5:
        print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row}]/td[{c_idx + 1}]").text, cur_price)


