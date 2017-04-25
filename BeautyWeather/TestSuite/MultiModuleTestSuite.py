# -*- coding:utf-8 -*-

import unittest

from BW_TestCase.WeatherModel import WeatherModel
from BW_TestCase.LoginModel import LoginModel

class MultiLoginTestSuite(unittest.TestCase):
    def testLoginModel1(self):
        #声明测试套
        RegisterSuite = unittest.TestSuite()
        #添加到测试套
        RegisterSuite.addTest(LoginModel("testLogin001"))

        RegisterSuite.addTest(unittest.makeSuite(WeatherModel("testWeather001")))
        #执行测试套
        unittest.TextTestRunner.run(RegisterSuite)

if __name__ == '__main__':
    unittest.main

