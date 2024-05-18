import pytest

import sys
# print(sys.path)
sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH")
from hybrid_framework.PageObjects.nop_login import login
from hybrid_framework.Utilities.ReadConfig import Read_config
from  hybrid_framework.Utilities.custom_log import custom_logger
ss_folder = r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\ScreenShots"

class Test_Login_001:
    log = custom_logger()
    @pytest.mark.sanity
    def test_verify_title(self, launch_browser):
        driver = launch_browser
        self.log.info("TC1: Nop Commerce verify launch page title")
        if driver.title == "Your store. Login":
            self.log.info("TC1: Nop Commerce verify launch page title = PASSED")
            assert True
        else:
            self.log.info("TC1: Nop Commerce verify launch page title = FAILED")
            driver.save_screenshot(ss_folder+"\\"+"test_verify_title.png")
            assert False

    @pytest.mark.regression
    def test_verify_dashbord(self, launch_browser):
        self.log.info("TC1: Nop Commerce verify dashbord page title")
        driver = launch_browser
        self.log.info("TC1: Browser lauched successfully")
        login_obj=login(driver)
        login_obj.SetEmail(Read_config.GetUser())
        login_obj.SetPassword(Read_config.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC1: Logged into the dashbord page")

        if driver.title=="Dashboard / nopCommerce administration":
            self.log.info("TC1: Nop Commerce verify dashbord page title =  Passed")
            assert True
        else:
            self.log.info("TC1: Nop Commerce verify dashbord page title =  Failed")
            driver.save_screenshot(ss_folder + "\\" + "test_verify_dashbord.png")
            assert False

