# -*- coding:UTF-8 -*- #coding:utf-8 #中文字符支持的正规写法和简写
#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:首页
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from utils.GetAppiumDriver import GetAppiumDriver
from utils.GetAppiumHelp import GetAppiumHelp

class HomePageIndex(object):
    def __init__(self):
        self.conn = GetAppiumDriver().driver
    def HomeBtn_XPath(self):
        HomeBtn_XPath = self.conn.find_element_by_xpath()
        return HomeBtn_XPath
    def HomeBtn_By_Id(self):
        HomeBtn_By_Id = self.conn.find_elements_by_id("com.subject.zhongchou:id/item_name")[3]
        return HomeBtn_By_Id
    def HomeBtn_by_Class_Name(self):
        HomeBtn_by_Class_Name = self.conn.find_elements_by_class_name("android.widget.CheckedTextView")[3]
        return HomeBtn_by_Class_Name
    def HomeBtn_Android_Uiautomator(self):
        HomeBtn_Android_Uiautomator = self.conn.find_element_by_android_uiautomator("new UiSelector().text(\"我的\")")
        return HomeBtn_Android_Uiautomator

if __name__ == '__main__':
    pass