#-*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
from Utils.GetAppiumDriver import GetAppiumDriver

class LoginPageIndex(object):
    def __init__(self):
        self.conn = GetAppiumDriver().driver

    def LoginPage_Text_Usr_By_Id(self):
        try:
            LoginPage_Text_Usr_By_Id = self.conn.find_element_by_id("com.icoolme.android.weather:dimen/text_md")
        except Exception as err:
            assert False,\
                "Can not locate the loginBtn，By ID"
        return LoginPage_Text_Usr_By_Id

    def LoginPage_Text_Pwd_By_Id(self):
        try:
            LoginPage_Text_Pwd_By_Id = self.conn.find_element_by_id("com.icoolme.android.weather:dimen/weather_last_update_time_stamp_textsize")
        except Exception as err:
            assert False,"Can not locate the loginBtn，By ID"
        return LoginPage_Text_Pwd_By_Id

    def LoginPage_Text_Usr_Uiautotor(self):
        try:
            LoginPage_Text_Usr_Uiautotor = self.conn.find_element_by_android_uiautomator("new UiSelector().text(\"请输入手机号/邮箱\")")
        except Exception as err:
            assert False,"Can not locate the loginBtn，Uiautomator"
        return LoginPage_Text_Usr_Uiautotor
    def LoginPage_Btn_by_Id(self):
        try:
            LoginPage_Btn_by_Id = self.conn.find_element_by_id("com.icoolme.android.weather:dimen/city_image_view_height_5x2")
        except Exception as err:
            assert False,"Can not locate the loginBtn，By ID"
        return LoginPage_Btn_by_Id
if __name__ == '__main__':
    pass

