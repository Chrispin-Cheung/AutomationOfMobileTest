# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.17
#Funciton:生成测试报告，调用HTMLTestRunner
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:


import traceback
import HTMLTestRunner
from io import StringIO

class CreateTestReport(object):
    def HtmlReporterDriver(self,htmlfilename,revtitle,revdesc,revsuite):
        file = "../TestWeatherReport/"+htmlfilename
        with open(file,'wb') as htmlstream:
            HTMLTestRunner.HTMLTestRunner(
                stream=htmlstream,
                verbosity=3,  #报告等级级别 1、无论几条case，只会返回一个结果无具体信息。返回结果三种情况
                                # 预期与实际不一致，fail
                                # 预期与实际一致    pass
                                # 程序错误         err
                                #
                                #        2、
                                #        3、
                title=revtitle,
                description=revdesc, #具体case具体描述
            ).run(revsuite)


     #截取控制台信息，并写入log
    def logToFile(self,_fname):
        fileName = "../TestWeatherLog/"+_fname+".txt"
        # fp = StringIO.StringIO()  #创建内存文件对象  python2 的用法
        fp = StringIO()
        traceback.print_exc(file=fp)
        message = fp.getvalue()
        curtime = time.strftime('%Y-%m-%d-%H:%M:%S-%A',time.localtime(time.time()))
        file = open(fileName,'a')
        file.writelines(curtime+"\n")
        file.write(message)#执行写入
        file.writelines(
            "=========================================================================================================\n")
        file.close()

if __name__ == '__main__':
    pass
# CreateTestReport().logToFile("test")