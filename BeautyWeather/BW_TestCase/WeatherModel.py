# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:天气测试用例集
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


def setUpModule():
    print("setUpModule")
def tearDoenmodule():
    print("tearDownModule")

class WeatherModel(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase

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

     # 功能点测试用例方法的命名模式，方法以test开头，后跟实现用例的方法和命名
    def testWeather001(self):
        pass

    def testWeather002(self):
        pass


if __name__ == "__main__":
    unittest.main()

