# -*- coding:utf-8 -*-
import time
import unittest

import os
import sys
os.getcwd()
sys.path.append(os.getcwd())

from BW_TestCase.LoginModel_TC import LoginModel_TC
from Utils.CreateTestReport import CreateTestReport
from Utils.SendEmailModel import SendEmailModel

class LoginTestSuite(unittest.TestCase):

    def testLoginsuite(self):
        print("Suite")
        loginsuite = unittest.TestSuite()

        loginsuite.addTest(LoginModel_TC("testLogin001"))
        loginsuite.addTest(LoginModel_TC("testLogin002"))
        # loginsuite.addTest(LoginModel_RXML("testLogin001"))
        # loginsuite.addTest(unittest.makeSuite(LoginModel_RXML("testLogin002"))) #notice makeSuite()


        #get the localtime
        timestr = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))

        fname = "testLogin"+timestr+".html"
        title = "Test Report"
        desc = "Result for test of Login and Logout"
        CreateTestReport().HtmlReporterDriver(fname,title,desc,loginsuite)
        SendEmailModel().MKEmailSiteDriver(fname)

if __name__ == '__main__':
    unittest.main()

