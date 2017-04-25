# -*- coding:utf-8 -*-

import unittest
from BW_TestCase.LoginModel_Plus import LoginModel_Plus


class SingleLoginSuite(unittest.TestCase):
    # #测试套使用方法一，适用与单模块和多模块方法
    def testLoginModel1(self):
        #定义一个测试套，命名为login01suite
        Login01suite = unittest.TestSuite()
        #添加测试套测试用例
        Login01suite.addTest(LoginModel_Plus("testLogin001"))
        Login01suite.addTest(LoginModel_Plus("testLogin002"))
    #     #执行测试套
    #     unittest.TextTestRunner.run(login01suite)
    # #测试套使用方法二 仅适用与单模块，模块之间没有业务关联
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



