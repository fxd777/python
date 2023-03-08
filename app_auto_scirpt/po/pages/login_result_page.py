from app_auto_scirpt.po.base_page.base_page import *
from selenium.webdriver.common.by import By


class res:
    login_name_loc=(By.ID,'me.onehome.app:id/tv_user_name')

    pass


class login_result_page(base_page):
    def get_login_name(self):
        return self.search_element(res.login_name_loc).text