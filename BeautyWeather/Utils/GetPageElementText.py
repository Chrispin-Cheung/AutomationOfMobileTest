# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:Appium Assert定义封装 断言
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from Utils.GetAppiumDriver import GetAppiumDriver

class GetPageElementText(object):
    def __init__(self):
        self.conn = GetAppiumDriver().driver

    def get_id(self,rev):
        get_id =  self.conn.find_element_by_id(rev)
        return get_id
    def get_class_name(self):
        pass
    def get_xpath(self):
        pass
    def get_ids(self):
        pass
    def get_class_names(self):
        pass
    def get_uiautomator(self):
        pass

if __name__ == '__main__':
    pass
