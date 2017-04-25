#-*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:立即体验页面
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from utils.GetAppiumDriver import GetAppiumDriver
from utils.GetAppiumHelp import GetAppiumHelp

class MyPageIndex(object):
    def __init__(self):
        self.dr = GetAppiumDriver().driver

    def MyIcon_Btn_by_Id(self):
       MyIcon_Btn_by_Id = self.dr.find_element_by_id("com.subject.zhongchou:id/bt")
       return MyIcon_Btn_by_Id

    def MyIcon_Btn_by_Name(self):
        MyIcon_Btn_by_Name = self.dr.find_element_by_class_name("android.widget.Button")
        return MyIcon_Btn_by_Name