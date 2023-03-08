from app_auto_scirpt.po.base_page.base_page import *
from selenium.webdriver.common.by import By




class res:
    login_button_enter_loc=(By.ID,'me.onehome.app:id/iv_user_head')

    pass



class my_page(base_page):
    def click_login_button_enter(self):
        self.click_element(res.login_button_enter_loc)
        pass