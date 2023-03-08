'''
此脚本实现优顾app的登录功能,使用的是PO模式+ddt+unittest+appium。
'''
from appium import webdriver
import unittest
import time
from app_auto_scirpt.po.pages.login_result_page import *
from app_auto_scirpt.po.pages.login_pages import *
from app_auto_scirpt.po.pages.home_page import *
from app_auto_scirpt.po.pages.my_page import *
from app_auto_scirpt.po.pages.first_page import *
import ddt
import read_data
import logging


read_yaml_result=read_data.YamlData().read_yaml_data(r'E:\pychon-code\app_auto_scirpt\data\login_account_number.yaml')
print(read_yaml_result)


@ddt.ddt
class onehome_login_po(unittest.TestCase):
    def setUp(self):
        caps = {
            "platformName": "android",
            "platformVersion": "5.1.1",
            "deviceName": "test103",
            "automationName": "UiAutomator1",
            "appPackage": "me.onehome.app",
            "appActivity": "me.onehome.app.activity.ActivityGuide"
        }

        # 生成对应的driver
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        pass
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        pass

    @ddt.data(*read_yaml_result)
    @ddt.unpack
    def test_login_yijia(self,username,pwd,login_result):
        driver=self.driver
        driver.implicitly_wait(30)
        try:
            first_page(driver).tong_yi_tiao_kuan()
            first_page(driver).li_ji_kai_qi()

            home_page(driver).click_my()

            my_page(driver).click_login_button_enter()

            login_page(driver).click_account_passwd_switch()
            login_page(driver).input_username(username)
            login_page(driver).input_passwd(pwd)
            login_page(driver).check_box()
            login_page(driver).click_login_button()
        except Exception as f:
            driver.get_screenshot_as_file(r'E:\pychon-code\app_auto_work\picture\yijia_info.png')
            logging.debug('Login failed')

        result_1=login_result_page(driver).get_login_name()
        driver.get_screenshot_as_file(r'E:\pychon-code\app_auto_work\picture\yijia_info.png')  #截取成功登录后的截图
        self.assertEqual(result_1,login_result)
        logging.debug('say with certainty')  #‘断言’    日志

        pass
if __name__ == '__main__':
    unittest.main()
