from app_auto_scirpt.po.base_page.base_page import *
from selenium.webdriver.common.by import By


class res:
    tong_yi_tiao_kuan_loc=(By.ID,"me.onehome.app:id/tv_agree")
    li_ji_kai_qi_loc='text("立即开启")'
    pass



class first_page(base_page):

    def tong_yi_tiao_kuan(self):  #同意条款
        self.click_element(res.tong_yi_tiao_kuan_loc)

    def li_ji_kai_qi(self):  #立即开启
        self.click_element_text(res.li_ji_kai_qi_loc)



