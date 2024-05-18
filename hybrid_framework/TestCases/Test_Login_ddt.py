import pytest

from hybrid_framework.PageObjects.nop_login import login
from hybrid_framework.Utilities.ReadConfig import Read_config
from hybrid_framework.Utilities.custom_log import custom_logger
from hybrid_framework.TestData.load_data import fetch_data_from_xl

ss_folder = r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\ScreenShots"
xl_file = r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\TestData\LoginData.xlsx"
class Test_suite_Login_DDT:
    log=custom_logger()
    @pytest.mark.sanity
    @pytest.mark.parametrize("email, pswd, expected", fetch_data_from_xl(xl_file, "Sheet1"))
    def test_verify_Login_ddt(self, launch_browser, email, pswd, expected):
        self.log.info("TC1_DDT: Nop Commerce verify dashboard page title")
        driver = launch_browser
        self.log.info("TC1_DDT: Browser launched successfully")
        login_obj = login(driver)
        login_obj.SetEmail(email)
        login_obj.SetPassword(pswd)
        login_obj.ClickLogin()
        self.log.info("TC1_DDT: Logged into the dashboard page")

        # if expected=="Pass":
        #     if driver.title=="Dashboard / nopCommerce administration":
        #         self.log.info("TC1: Nop Commerce verify dashbord page title =  Passed")
        #         assert True
        #     else:
        #         self.log.info("TC1: Nop Commerce verify dashbord page title =  Failed")
        #         driver.save_screenshot(ss_folder + "\\" + "test_verify_dashbord.png")
        #         assert False
        # else:
        #     if driver.title!="Dashboard / nopCommerce administration":
        #         self.log.info("TC1: Nop Commerce verify dashbord page title =  Passed")
        #         assert True
        #     else:
        #         self.log.info("TC1: Nop Commerce verify dashbord page title =  Failed")
        #         driver.save_screenshot(ss_folder + "\\" + "test_verify_dashbord.png")
        #         assert False

        if driver.title=="Dashboard / nopCommerce administration" and expected=="Pass":
            self.log.info(f"TC1_DDT: Nop Commerce verify dashboard page title {email} {pswd} =  Passed")
            assert True
        elif driver.title!="Dashboard / nopCommerce administration" and expected=="Fail":
            self.log.info(f"TC1_DDT: Nop Commerce verify dashboard page title {email} {pswd} =  Passed")
            assert True
        else:
            self.log.info(f"TC1_DDT: Nop Commerce verify dashboard page title {email} {pswd} =  Failed")
            driver.save_screenshot(ss_folder + "\\" + "test_verify_dashbord_ddt.png")
            assert False
