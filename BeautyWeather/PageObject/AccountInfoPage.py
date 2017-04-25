#-*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:账户信息页面
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from Utils.GetAppiumDriver import GetAppiumDriver

class AccountInfoPage(object):
    def __init__(self):
        self.dr = GetAppiumDriver().driver
    def LogoutBtn_Id(self):
        try:
            LogoutBtn_Id = self.dr.find_element_by_id("com.icoolme.android.weather:id/uac_account_logout_btn")
        except Exception as err:
            assert False,"账户信息页未定位到退出登录按钮，By_Id"
        return LogoutBtn_Id
    def LogoutBtn_uiautomator(self):
        try:
            LogoutBtn_uiautomator = self.dr.find_element_by_android_uiautomator("new UiSelector().text(\"退出登录\")")
        except Exception as err:
            assert False,"账户信息页为定位到退出登录按钮，By_Uiautomator"
        return LogoutBtn_uiautomator
