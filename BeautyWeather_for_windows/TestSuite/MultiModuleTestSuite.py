# -*- coding:utf-8 -*-

import unittest

from BW_TestCase.WeatherModel import WeatherModel
from BW_TestCase.LoginModel import LoginModel

class MultiLoginTestSuite(unittest.TestCase):
    def testLoginModel1(self):

        RegisterSuite = unittest.TestSuite()

        RegisterSuite.addTest(LoginModel("testLogin001"))

        RegisterSuite.addTest(unittest.makeSuite(WeatherModel("testWeather001")))

        unittest.TextTestRunner.run(RegisterSuite)

if __name__ == '__main__':
    unittest.main

