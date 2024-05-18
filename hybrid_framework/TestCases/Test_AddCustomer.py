import random
import string

import pytest
import sys
# print(sys.path)
sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH")
from hybrid_framework.PageObjects.nop_login import login
from hybrid_framework.PageObjects.addcustomer import AddCustomer
from hybrid_framework.Utilities.ReadConfig import Read_config
from  hybrid_framework.Utilities.custom_log import custom_logger
ss_folder = r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\ScreenShots"

class Test_Add_Customer_003:
    log = custom_logger()
    @pytest.mark.regression
    def test_verify_addcustomer(self, launch_browser):
        self.log.info("TC3: Nop Commerce verify Add Customer")
        driver = launch_browser
        self.log.info("TC3: Browser lauched successfully")
        login_obj=login(driver)
        login_obj.SetEmail(Read_config.GetUser())
        login_obj.SetPassword(Read_config.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC3: Navigated to dashbord page")
        ac_obj = AddCustomer(driver)
        ac_obj.NavigateCustomerPage()
        ac_obj.ClickAddNewCustomer()
        ####generat
        email = []
        for i in range(8):
            email.append(random.choice(string.ascii_letters + string.digits))

        ac_obj.SetUsername("".join(email)+"@gmail.com")
        ac_obj.SetPasword("abcdef")
        ac_obj.SetFirstname("ram")
        ac_obj.SetLastname("sam")
        ac_obj.selectGender("male")
        ac_obj.SetDOB("05-05-2024")
        ac_obj.SetCompanyName("xyz company")
        ac_obj.SelectNewsLetter("Your store name")
        ac_obj.SelectCustomerRole("Administrators")
        ac_obj.SelectVendor("Vendor 1")
        ac_obj.ClickActive()
        ac_obj.SetAdminComment("this is admin msg")
        ac_obj.ClickSave()
        alt_msg = ac_obj.VerifyAlert()
        print(alt_msg)
        if "The new customer has been added successfully" in alt_msg:
            self.log.info("TC3: Nop Commerce verify Add Customer = PASSED")
            assert True
        else:
            self.log.info("TC3: Nop Commerce verify Add Customer = FAILED")
            driver.save_screenshot(ss_folder + "\\" + "test_verify_addcustomer.png")
            assert False