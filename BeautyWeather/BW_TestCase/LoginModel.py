# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:登录单测试用例执行
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
import time
import unittest

from Utils.GetAppiumDriver import GetAppiumDriver
from Utils.GetAppiumHelp import GetAppiumHelp
from Utils.ReadXMLDriver import ReadXMLDriver

from PageObject.HomePageIndex import HomePageIndex
from PageObject.MyPageIndex import MyPageIndex
from PageObject.LoginPageIndex import LoginPageIndex



class LoginModel(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase
    #-------用例的构建和销毁-------
    #--用例执行初始化--
    def setUp(self):
        self.driver = GetAppiumDriver().driver
        # time.sleep(20)
        time.sleep(20)
        for i in range(2):
            GetAppiumHelp().tap()
            time.sleep(2)

     # 功能点测试用例方法的命名模式，方法以test开头，后跟实现用例的方法和命名
    def testLogin001(self):
        HomePageIndex().HomeBtn_Android_Uiautomator().click()
        time.sleep(2)
        MyPageIndex().MyLoginText_by_Id().click()
        time.sleep(2)
        LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys("18983838625")
        #LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys(ReadXMLDriver().returnXMLfile("LoginData.xml","LoginData","Login001"))
        time.sleep(2)
        LoginPageIndex().LoginPage_Text_Pwd_By_Id().send_keys("12345678")
        time.sleep(2)
        LoginPageIndex().LoginPage_Btn_by_Id().click()
        time.sleep(2)

        expValue = "CC83483282"
        actValue = MyPageIndex().MyLoginText_by_Id().text
        msg="登录测试失败"
        self.assertEqual(expValue,actValue,msg) #fail, if expValue != actValue,and print (msg)
        # self.assertEqual(expValue,actValue)


    #--用例执行完后善后操作（结束并清理）--
    def tearDown(self):
        self.driver.quit()# end the server.session
        print("Login Test Ended")

    #---self added functions and methods


if __name__ == "__main__":
    unittest.main()

