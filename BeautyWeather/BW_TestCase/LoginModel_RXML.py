# -*- coding:utf-8 -*-

import time
import unittest
from Utils.GetAppiumDriver import GetAppiumDriver
from Utils.GetAppiumHelp import GetAppiumHelp

from PageObject.HomePageIndex import HomePageIndex
from PageObject.MyPageIndex import MyPageIndex
from PageObject.LoginPageIndex import LoginPageIndex
from PageObject.AccountInfoPage import AccountInfoPage

class LoginModel_RXML(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print ("setUpClass")
        cls.driver = GetAppiumDriver().driver
        time.sleep(20)

        for i in range(2):
            GetAppiumHelp().tap()
            time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver = GetAppiumDriver().driver
        cls.driver.quit()
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")
        try:
            if MyPageIndex().MyLoginText_by_Id().text == "CC83483282" :
                #enter into the accountinfopage
                MyPageIndex().MyLoginText_by_Id().click()
                AccountInfoPage().LogoutBtn_Id().click()
        except:
            pass






    def testLogin001(self):

        HomePageIndex().HomeBtn_By_Id().click()
        time.sleep(1)

        MyPageIndex().MyLoginText_by_Id().click()
        time.sleep(1)

        LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys("18983838625")
        time.sleep(1)

        LoginPageIndex().LoginPage_Text_Pwd_By_Id().send_keys("12345678")
        time.sleep(1)

        LoginPageIndex().LoginPage_Btn_by_Id().click()
        time.sleep(2)

        expValue = "CC83483282"
        actValue = MyPageIndex().MyLoginText_by_Id().text
        self.assertEqual(expValue,actValue)

    def testLogin002(self):
        HomePageIndex().HomeBtn_By_Id().click()
        time.sleep(1)

        MyPageIndex().MyLoginText_by_Id().click()
        time.sleep(1)

        LoginPageIndex().LoginPage_Text_Usr_Uiautotor().send_keys("18983838625")
        time.sleep(1)

        LoginPageIndex().LoginPage_Text_Pwd_By_Id().send_keys("12345678")
        time.sleep(2)

        LoginPageIndex().LoginPage_Btn_by_Id().click()
        time.sleep(2)

        expValue = "CC83483282"
        actValue = MyPageIndex().MyLoginText_by_Id().text
        self.assertEqual(expValue,actValue)
