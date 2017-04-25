#-*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
import os
import sys
os.getcwd()
sys.path.append(os.getcwd())
from Utils.GetAppiumDriver import GetAppiumDriver

class RES(object):
    HomeBtn_By_Id = "com.icoolme.android.weather:id/home_tab_me_icon"
    HomeBtn_xpath = "//android.widget.ImageView[@text=\"我\"]"
    #HomeBtn_xpath = "//android.widget.ImageView[@text='我']"
    HomeBtn_by_Class_Name = "android.widget.ImageView"
    HomeBtn_Android_Uiautomator = "new UiSelector().text(\"我\")"

class HomePageIndex(object):
    def __init__(self):
        self.conn = GetAppiumDriver().driver

    def HomeBtn_By_Id(self):
        try:
            HomeBtn_By_Id = self.conn.find_element_by_id(RES().HomeBtn_By_Id)

        except Exception as err:
            assert False,\
            "Can not locate myBtn，By_id"
        return HomeBtn_By_Id


    def HomeBtn_by_Class_Name(self):
        try:
            HomeBtn_by_Class_Name = self.conn.find_elements_by_class_name(RES().HomeBtn_by_Class_Name)[3] #fail,can't use
        except Exception as err:
            assert False,\
                "Can not locate myBtn，By_class_name"
            return HomeBtn_by_Class_Name

    def HomeBtn_Android_Uiautomator(self):
        try:
            HomeBtn_Android_Uiautomator = self.conn.find_element_by_android_uiautomator(RES().HomeBtn_Android_Uiautomator)
        except:
            assert False,\
                "Can not locate myBtn，By_Uiautomator"
        return HomeBtn_Android_Uiautomator
    def HomeBtn_xpath(self):
        try:
            HomeBtn_xpath = self.conn.find_elements_by_xpath(RES().HomeBtn_xpath)
        except Exception as err:
            assert False,"Can not locate myBtn，By_xpath"
        return HomeBtn_xpath
if __name__ == '__main__':
    pass
