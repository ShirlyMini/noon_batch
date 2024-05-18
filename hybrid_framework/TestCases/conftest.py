import pytest
from selenium import webdriver
import sys
# print(sys.path)
sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH")
from hybrid_framework.Utilities.ReadConfig import Read_config

@pytest.fixture()
def launch_browser(request):
    browser=request.config.getoption("--browser")
    # print(browser)
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(Read_config.GetURL())
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")

# def pytest_configure(config):
#     config._metadata={
#     "Tester":"shirly",
#     "ModuleName":"customers",
#     "ProjectName":"nopcommerce",
#     }
def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: this is a tag name for sanity test cases")
    config.addinivalue_line("markers", "regression: this is a tag name for regression test cases")