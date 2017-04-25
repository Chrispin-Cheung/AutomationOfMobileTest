#-*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:我的页面
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from Utils.GetAppiumDriver import GetAppiumDriver

class MyPageIndex(object):
    def __init__(self):
        self.dr = GetAppiumDriver().driver

    def MyIcon_Btn_by_Id(self):# Failed
       try:
            MyIcon_Btn_by_Id = self.dr.find_element_by_id("com.icoolme.android.weather:id/login_icon")
       except Exception as err:
           assert False,"我的页面未定位到账户登录,by_id"
       return MyIcon_Btn_by_Id
    #
    # def MyIcon_Btn_by_Name(self):
    #     MyIcon_Btn_by_Name = self.dr.find_element_by_class_name("android.widget.Button")
    #     return MyIcon_Btn_by_Name
    def MyPageBtn_Android_Uiautomator(self):
        try:
            MyPageBtn_Android_Uiautomator = self.dr.find_element_by_android_uiautomator("new UiSelector().text(\"登录帐号\")")
        except Exception as err:
            assert False,"我的页面为定位到账户登录,by_Uiautomator"
        return MyPageBtn_Android_Uiautomator
    def MyLoginText_by_Id(self):
        try:
            MyLoginText_by_Id = self.dr.find_element_by_id("com.icoolme.android.weather:id/login_text")
        except Exception as err:
            assert False,"我的页面为定位到账户登录，by_id"
        return MyLoginText_by_Id
