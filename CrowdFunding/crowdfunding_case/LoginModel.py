# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:登录测试用例
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
import time
import unittest
from utils.GetAppiumDriver import GetAppiumDriver
from utils.GetAppiumHelp import GetAppiumHelp
from business.LJTYPageIndex import LJTYPageIndex
from business.HomePageIndex import HomePageIndex
from business.MyPageIndex import MyPageIndex
class LoginModel(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase
    #-------用例的构建和销毁-------
    #--用例执行初始化--
    def setUp(self):
        self.driver = GetAppiumDriver().driver
        time.sleep(4)
        for i in range(3):
            GetAppiumHelp().right_to_left()
            time.sleep(5)
        GetAppiumHelp().tap()
        LJTYPageIndex().LJTY_Btn_by_Id().click()
        time.sleep(3)
     # 功能点测试用例方法的命名模式，方法以test开头，后跟实现用例的方法和命名
    def testLogin001(self):
        HomePageIndex().HomeBtn_Android_Uiautomator().click()
        time.sleep(3)
    def testlogin002(self):
        MyPageIndex().MyIcon_Btn_by_Name().click()

    def assertEqual(self, first, second, msg=None):
        pass

    #--用例执行完后善后操作（结束并清理）--
    def tearDown(self):
        pass

    #---self added functions and methods

if __name__ == "__main__":
    unittest.main
