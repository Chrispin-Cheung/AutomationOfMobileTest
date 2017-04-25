# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.17
#Funciton:生成测试报告，调用HTMLTestRunner
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

import os
import sys
os.getcwd()
sys.path.append(os.getcwd())
import time
import traceback
from Utils.HTMLTestRunner import  HTMLTestRunner
from io import StringIO

class CreateTestReport(object):
    def HtmlReporterDriver(self,htmlfilename,revtitle,revdesc,revsuite):
        # file = "../TestWeatherReport/"+htmlfilename
        file = os.getcwd+r"TestWeatherReport\\" + htmlfilename
        with open(file,'wb') as htmlstream:
            HTMLTestRunner.HTMLTestRunner(
                stream=htmlstream,
                verbosity=3,
                title=revtitle,
                description=revdesc,
            ).run(revsuite)



    def logToFile(self,_fname):
        # fileName = "../TestWeatherLog/"+_fname+".txt"
        fileName ="..\TestWeatherLog\\" + _fname + '.txt'
        # fp = StringIO.StringIO()
        fp = StringIO()
        traceback.print_exc(file=fp)
        message = fp.getvalue()
        curtime = time.strftime('%Y-%m-%d-%H:%M:%S-%A',time.localtime(time.time()))
        file = open(fileName,'a')
        file.writelines(curtime+"\n")
        file.write(message)
        file.writelines(
            "=========================================================================================================\n")
        file.close()

if __name__ == '__main__':
    pass
# CreateTestReport().logToFile("test")