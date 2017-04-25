# -*- coding:utf-8 -*-
import os
import sys
os.getcwd()
sys.path.append(os.getcwd())
import unittest
from BW_TestCase.LoginModel_Plus import LoginModel_Plus


class SingleLoginSuite(unittest.TestCase):

    def testLoginModel1(self):

        Login01suite = unittest.TestSuite()

        Login01suite.addTest(LoginModel_Plus("testLogin001"))
        Login01suite.addTest(LoginModel_Plus("testLogin002"))
    #
    #     unittest.TextTestRunner.run(login01suite)
    # #
    # def testLoginModel2(self):
    #     Login01suite = unittest.TestSuite()
    #     Loginlist = ("testLogin001","testLogin002")
    #     for tmp in Loginlist:
    #         Login01suite.addTest(LoginModel_Plus(tmp))
    #     #unittest.TextTestRunner.run(Login01suite)
        from Utils.CreateTestReport import CreateTestReport
        filename = "logintest"
        title = u"登录模块测试用例报告"
        desc = u"测试报告"
        CreateTestReport().HtmlReporterDriver(filename,title,desc,Login01suite)
        # CreateTestReport.logToFile("logintest")


if __name__ == '__main__':
    unittest.main()



