from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://www.deadlinkcity.com/")

elems = driver.find_elements(By.XPATH, "//a")
for elm in elems:
    url = elm.get_attribute("href")
    try:
        status = requests.get(url)
        if int(status.status_code) >=299:
            print(f"Invalid {url}: {status.status_code}")
        else:
            print(f"Valid {url}: {status.status_code}")
    except:
        print(f"Invalid {url}: No status code")

