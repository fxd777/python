from app_auto_scirpt.po.base_page.base_page import *
from selenium.webdriver.common.by import By


class res:
    account_passwd_switch_loc=(By.ID,'me.onehome.app:id/rb_pw_login')
    username_loc=(By.ID,'me.onehome.app:id/et_login_number')
    passwd_loc=(By.ID,'me.onehome.app:id/et_login_password')
    login_button=(By.ID,'me.onehome.app:id/bt_fulfill')
    check_box_loc=(By.CLASS_NAME,'android.widget.CheckBox')
    # username = "18731333417"
    # passwd = "fengxiaodong777"


class login_page(base_page):
    def click_account_passwd_switch(self):  #切换到账号密码登录
        self.click_element(res.account_passwd_switch_loc)
        pass


    def input_username(self,username):   #对账号进行设置入参参数
        self.input_content(res.username_loc,username)
        pass

    def input_passwd(self,pwd):      #对密码进行设置入参参数
        self.input_content(res.passwd_loc,pwd)
        pass

    def check_box(self):
        self.click_element(res.check_box_loc)


    def click_login_button(self):    #登录按钮
        self.click_element(res.login_button)
        pass