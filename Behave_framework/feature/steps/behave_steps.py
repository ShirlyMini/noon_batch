from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given(u'Launch browser')
def step_impl(context):
    service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")  # (used to connect with webdriver)
    context.driver = webdriver.Chrome(service=service_obj)


@when(u'Open Nop Commerce login page')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")
    context.driver.maximize_window()


@then(u'Verify Login page title')
def step_impl(context):
    assert context.driver.title=='Your store. Login'


@when(u'Enter Username "{user}" and password "{pswd}"')
def step_impl(context, user, pswd):
    context.driver.find_element(By.NAME, "Email").clear()
    context.driver.find_element(By.NAME, "Email").send_keys(user)
    context.driver.find_element(By.NAME, "Password").clear()
    context.driver.find_element(By.NAME, "Password").send_keys(pswd)


@when(u'Click Login button')
def step_impl(context):
    context.driver.find_element(By.TAG_NAME, 'button').click()


@then(u'Verify Dashboard page')
def step_impl(context):
    assert context.driver.title=='Dashboard / nopCommerce administration'


@then(u'Verify Dashboard page as per login data "{status}"')
def step_impl(context, status):
    if status=="True":
        assert context.driver.title == 'Dashboard / nopCommerce administration'
    elif status=="False":
        assert context.driver.title != 'Dashboard / nopCommerce administration'
    else:
        assert False




