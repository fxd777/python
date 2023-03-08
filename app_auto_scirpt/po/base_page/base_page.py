'''
主要存放对元素定位方法的封装
'''

class base_page(object):
    def __init__(self,driver):
        self.driver=driver

    def search_element(self,loc):
        return self.driver.find_element(*loc)

    def search_element_text(self,loc):
        return self.driver.find_element_by_android_uiautomator(loc)

    def click_element(self,loc):
        self.search_element(loc).click()

    def click_element_text(self,loc):
        self.search_element_text(loc).click()

    def input_content(self,loc,text):
        self.search_element(loc).send_keys(text)

    def input_content_text(self,loc,text):
        self.search_element_text(loc).send_keys(text)


