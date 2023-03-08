from app_auto_scirpt.po.base_page.base_page import *
from selenium.webdriver.common.by import By

class res:
    login_head_loc='text("我的")'
    pass


class home_page(base_page):

    def click_my(self):
        self.click_element_text(res.login_head_loc)
        pass



