from time import sleep

import pytest
import sys
# print(sys.path)
sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH")
from hybrid_framework.PageObjects.nop_login import login
from hybrid_framework.PageObjects.addcustomer import AddCustomer
from hybrid_framework.PageObjects.SearchBy import SearchBy
from hybrid_framework.Utilities.ReadConfig import Read_config
from  hybrid_framework.Utilities.custom_log import custom_logger
ss_folder = r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\ScreenShots"

class Test_Search_003:
    log = custom_logger()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_by_email(self, launch_browser):
        self.log.info("TC4: Nop Commerce verify Search option using email")
        driver = launch_browser
        self.log.info("TC4: Browser launched successfully")
        login_obj = login(driver)
        login_obj.SetEmail(Read_config.GetUser())
        login_obj.SetPassword(Read_config.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC4: Navigated to dashboard page")
        ac_obj=AddCustomer(driver)
        ac_obj.NavigateCustomerPage()
        self.log.info("TC4: Navigated to customer page")

        search_obj = SearchBy(driver)
        search_obj.SetEmail("steve_gates@nopCommerce.com")
        search_obj.ClickSearch()
        sleep(7)
        email = search_obj.VerifyEmailSearch()
        if email=="steve_gates@nopCommerce.com":
            self.log.info("TC4: Nop Commerce verify Search option using email = PASSED")
            assert True
        else:
            self.log.info("TC4: Nop Commerce verify Search option using email = FAILED")
            driver.save_screenshot(ss_folder + "\\" + "test_search_by_email.png")
            assert False

    @pytest.mark.regression
    def test_search_by_firstname(self, launch_browser):
        self.log.info("TC4: Nop Commerce verify Search option using firstname")
        driver = launch_browser
        self.log.info("TC4: Browser launched successfully")
        login_obj = login(driver)
        login_obj.SetEmail(Read_config.GetUser())
        login_obj.SetPassword(Read_config.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC4: Navigated to dashboard page")
        ac_obj=AddCustomer(driver)
        ac_obj.NavigateCustomerPage()
        self.log.info("TC4: Navigated to customer page")

        search_obj = SearchBy(driver)
        search_obj.SetFirstName("James")
        search_obj.ClickSearch()
        sleep(5)
        status = search_obj.VerifyNameSearch("James")
        if status==True:
            self.log.info("TC4: Nop Commerce verify Search option using firstname = PASSED")
            assert True
        else:
            self.log.info("TC4: Nop Commerce verify Search option using firstname = FAILED")
            driver.save_screenshot(ss_folder + "\\" + "test_search_by_firstname.png")
            assert False
