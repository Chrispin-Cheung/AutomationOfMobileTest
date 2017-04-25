# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:登录测试多用例场景关联顺序执行
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
import os
import re
import sys
import time
import datetime
import unittest
import HTMLTestRunner

from Utils.GetAppiumDriver import GetAppiumDriver
from Utils.GetAppiumHelp import GetAppiumHelp

from PageObject.HomePageIndex import HomePageIndex
from PageObject.MyPageIndex import MyPageIndex
from PageObject.LoginPageIndex import LoginPageIndex
from PageObject.AccountInfoPage import AccountInfoPage
from Utils.SendEmailModel import SendEmailModel

# class RES(object):
#     username = ""


# def setUpModule():
#     print("setUpModule")
# def tearDownModule():
#     print("tearDownModule")

class LoginModel_Plus(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print ("setUpClass")
        cls.driver = GetAppiumDriver().driver

        # time.sleep(20)
        time.sleep(20)
        for i in range(2):
            GetAppiumHelp().tap()
            time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver = GetAppiumDriver().driver
        cls.driver.quit()
        print("tearDownClass")

    #-------用例的构建和销毁-------
    #--用例执行初始化--
    def setUp(self):
        print("setUp")

     #--用例执行完后善后操作（结束并清理）--
    def tearDown(self):
        print("tearDown")
        try:
            if MyPageIndex().MyLoginText_by_Id().text == "CC83483282" :
                #enter into the accountinfopage
                MyPageIndex().MyLoginText_by_Id().click()
                AccountInfoPageIndex().LogoutBtn_Id().click()
        except:
            pass





     # 功能点测试用例方法的命名模式，方法以test开头，后跟实现用例的方法和命名
    def testLogin001(self):
        #Homepage click the my tab
        HomePageIndex().HomeBtn_By_Id().click()
        time.sleep(2)
        #MyPage click the login button
        MyPageIndex().MyLoginText_by_Id().click()
        time.sleep(2)
        #input username
        LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys("18983838625")
        time.sleep(2)
        #input password
        LoginPageIndex().LoginPage_Text_Pwd_By_Id().send_keys("12345678")
        time.sleep(2)
        # Login click
        LoginPageIndex().LoginPage_Btn_by_Id().click()
        time.sleep(2)

        expValue = "CC83483282"
        actValue = MyPageIndex().MyLoginText_by_Id().text
        #msg="登录测试失败"
        # self.assertEqual(expValue,actValue,msg) #fail, if expValue != actValue,and print (msg)
        self.assertEqual(expValue,actValue)

    def testLogin002(self):
        HomePageIndex().HomeBtn_By_Id().click()
        time.sleep(2)
        #MyPage click the login button
        MyPageIndex().MyLoginText_by_Id().click()
        time.sleep(2)
        #input username
        LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys("18983838625")
        time.sleep(2)
        #input password
        LoginPageIndex().LoginPage_Text_Pwd_By_Id().send_keys("12345678")
        time.sleep(2)
        # Login click
        LoginPageIndex().LoginPage_Btn_by_Id().click()
        time.sleep(2)

        expValue = "CC83483282"
        actValue = MyPageIndex().MyLoginText_by_Id().text
        #msg="登录测试失败"
        # self.assertEqual(expValue,actValue,msg) #fail, if expValue != actValue,and print (msg)
        self.assertEqual(expValue,actValue)



    #---self added functions and methods


if __name__ == "__main__":        #运行测试套时，需要注释掉
    # pass
    #unittest.main()
    #          #运行测试套时，需要注释掉
    pass
    # suite = unittest.TestSuite()
    # suite.addTest(LoginModel_Plus("testLogin001"))
    # suite.addTest(LoginModel_Plus("testLogin002"))
    #
    # from Utils.CreateTestReport import CreateTestReport
    # filename = "logintest1.html"
    # title = u"登录模块测试用例报告"
    # desc = u"测试报告"
    # CreateTestReport().HtmlReporterDriver(filename,title,desc,suite)
    # SendEmailModel().MKEmailSiteDriver(filename)

 #
    # #get the localtime
    #timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = "../TestWeatherReport/result_" + timestr + ".html"
    # print(filename)
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     tltle='测试结果',
    #     description='测试报告'
    # )
    # # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #引入测试报告生成模块